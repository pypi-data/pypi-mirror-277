# ------------------------------------------------------------------------------
# Copyright (c) 2022 Korawich Anuttra. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for
# license information.
# ------------------------------------------------------------------------------
from __future__ import annotations

import inspect
import logging
import subprocess
from abc import ABC, abstractmethod
from datetime import date, datetime
from inspect import Parameter
from subprocess import CompletedProcess
from typing import Any, Callable, Literal, Optional, Union

from ddeutil.io.models.lineage import dt_now
from pydantic import BaseModel, Field
from pydantic.functional_validators import model_validator
from typing_extensions import Self

from .__regex import RegexConf
from .__types import DictData
from .exceptions import PyException, TaskException
from .loader import Loader, map_params
from .utils import make_registry


class BaseStage(BaseModel, ABC):
    """Base Stage Model."""

    id: Optional[str] = None
    name: str

    @abstractmethod
    def execute(self, params: DictData) -> DictData:
        raise NotImplementedError("Stage should implement ``execute`` method.")

    def set_outputs(self, rs: DictData, params: DictData) -> DictData:
        """Set outputs to params"""
        if self.id is None:
            return params

        if "stages" not in params:
            params["stages"] = {}

        params["stages"][self.id] = {"outputs": rs}
        return params


class EmptyStage(BaseStage):
    """Empty stage that is doing nothing and logging the name of stage only."""

    def execute(self, params: DictData) -> DictData:
        """Execute for the Empty stage that do only logging out."""
        logging.info(f"Execute: {self.name!r}")
        return params


class ShellStage(BaseStage):
    """Shell statement stage."""

    shell: str
    env: dict[str, str] = Field(default_factory=dict)

    @staticmethod
    def __prepare_shell(shell: str):
        """Prepare shell statement string that include newline"""
        return shell.replace("\n", ";")

    def set_outputs(self, rs: CompletedProcess, params: DictData) -> DictData:
        """Set outputs to params"""
        # NOTE: skipping set outputs of stage execution when id does not set.
        if self.id is None:
            return params

        if "stages" not in params:
            params["stages"] = {}

        params["stages"][self.id] = {
            # NOTE: The output will fileter unnecessary keys from ``_locals``.
            "outputs": {
                "return_code": rs.returncode,
                "stdout": rs.stdout,
                "stderr": rs.stderr,
            },
        }
        return params

    def execute(self, params: DictData) -> DictData:
        """Execute the Shell & Powershell statement with the Python build-in
        ``subprocess`` package.
        """
        rs: CompletedProcess = subprocess.run(
            self.__prepare_shell(self.shell),
            capture_output=True,
            text=True,
            shell=True,
        )
        if rs.returncode > 0:
            print(f"{rs.stderr}\nRunning Statement:\n---\n{self.shell}")
            # FIXME: raise err for this execution.
            # raise ShellException(
            #     f"{rs.stderr}\nRunning Statement:\n---\n"
            #     f"{self.shell}"
            # )
        self.set_outputs(rs, params)
        return params


class PyStage(BaseStage):
    """Python executor stage that running the Python statement that receive
    globals nad additional variables.
    """

    run: str
    vars: DictData = Field(default_factory=dict)

    def get_var(self, params: DictData) -> DictData:
        """Return variables"""
        rs = self.vars.copy()
        for p, v in self.vars.items():
            rs[p] = map_params(v, params)
        return rs

    def set_outputs(self, rs: DictData, params: DictData) -> DictData:
        """Set outputs to params"""
        # NOTE: skipping set outputs of stage execution when id does not set.
        if self.id is None:
            return params

        if "stages" not in params:
            params["stages"] = {}

        params["stages"][self.id] = {
            # NOTE: The output will fileter unnecessary keys from ``_locals``.
            "outputs": {k: rs[k] for k in rs if k != "__annotations__"},
        }
        return params

    def execute(self, params: DictData) -> DictData:
        """Execute the Python statement that pass all globals and input params
        to globals argument on ``exec`` build-in function.

        :param params: A parameter that want to pass before run any statement.
        :type params: DictData

        :rtype: DictData
        :returns: A parameters from an input that was mapped output if the stage
            ID was set.
        """
        _globals: DictData = globals() | params | self.get_var(params)
        _locals: DictData = {}
        try:
            exec(map_params(self.run, params), _globals, _locals)
        except Exception as err:
            raise PyException(
                f"{err.__class__.__name__}: {err}\nRunning Statement:\n---\n"
                f"{self.run}"
            ) from None

        # NOTE: set outputs from ``_locals`` value from ``exec``.
        self.set_outputs(_locals, params)
        return params | {k: _globals[k] for k in params if k in _globals}


class TaskSearch(BaseModel):
    """Task Search Model"""

    path: str
    func: str
    tag: str


class TaskStage(BaseStage):
    """Task executor stage that running the Python function."""

    task: str
    args: DictData

    @staticmethod
    def extract_task(task: str) -> Callable[[], Callable[[Any], Any]]:
        """Extract Task string value to task function."""
        if not (found := RegexConf.RE_TASK_FMT.search(task)):
            raise ValueError("Task does not match with task format regex.")
        tasks = TaskSearch(**found.groupdict())

        # NOTE: Registry object should implement on this package only.
        # TODO: This prefix value to search registry should dynamic with
        #   config file.
        rgt = make_registry(f"ddeutil.workflow.{tasks.path}")
        if tasks.func not in rgt:
            raise NotImplementedError(
                f"ddeutil.workflow.{tasks.path}.registries does not "
                f"implement registry: {tasks.func}."
            )

        if tasks.tag not in rgt[tasks.func]:
            raise NotImplementedError(
                f"tag: {tasks.tag} does not found on registry func: "
                f"ddeutil.workflow.{tasks.path}.registries."
                f"{tasks.func}"
            )
        return rgt[tasks.func][tasks.tag]

    def execute(self, params: DictData) -> DictData:
        """Execute the Task function."""
        task_caller = self.extract_task(self.task)()
        if not callable(task_caller):
            raise ImportError("Task caller function does not callable.")

        # NOTE: check task caller parameters
        ips = inspect.signature(task_caller)
        if any(
            k not in self.args
            for k in ips.parameters
            if ips.parameters[k].default == Parameter.empty
        ):
            raise ValueError(
                f"necessary parameters, ({', '.join(ips.parameters.keys())}), "
                f"does not set to args"
            )
        try:
            rs = task_caller(**map_params(self.args, params))
        except Exception as err:
            raise TaskException(f"{err.__class__.__name__}: {err}") from err
        self.set_outputs(rs, params)
        return params


# NOTE: Order of parsing stage data
Stage = Union[
    PyStage,
    ShellStage,
    TaskStage,
    EmptyStage,
]


class Strategy(BaseModel):
    """Strategy Model"""

    matrix: list[str] = Field(default_factory=list)
    include: list[str] = Field(default_factory=list)
    exclude: list[str] = Field(default_factory=list)


class Job(BaseModel):
    """Job Model"""

    stages: list[Stage] = Field(default_factory=list)
    needs: list[str] = Field(default_factory=list)
    strategy: Strategy = Field(default_factory=Strategy)

    def stage(self, stage_id: str) -> Stage:
        for stage in self.stages:
            if stage_id == (stage.id or ""):
                return stage
        raise ValueError(f"Stage ID {stage_id} does not exists")

    def execute(self, params: DictData | None = None) -> DictData:
        """Execute job with passing dynamic parameters from the pipeline."""
        for stage in self.stages:
            # NOTE:
            #       I do not use below syntax because `params` dict be the
            #   reference memory pointer and it was changed when I action
            #   anything like update or re-construct this.
            #       ... params |= stage.execute(params=params)
            stage.execute(params=params)
        return params


class BaseParams(BaseModel, ABC):
    """Base Parameter that use to make Params Model."""

    desc: Optional[str] = None
    required: bool = True
    type: str

    @abstractmethod
    def receive(self, value: Optional[Any] = None) -> Any:
        raise ValueError(
            "Receive value and validate typing before return valid value."
        )


class DefaultParams(BaseParams):
    """Default Parameter that will check default if it required"""

    default: Optional[str] = None

    @abstractmethod
    def receive(self, value: Optional[Any] = None) -> Any:
        raise ValueError(
            "Receive value and validate typing before return valid value."
        )

    @model_validator(mode="after")
    def check_default(self) -> Self:
        if not self.required and self.default is None:
            raise ValueError(
                "Default should set when this parameter does not required."
            )
        return self


class DatetimeParams(DefaultParams):
    """Datetime parameter."""

    type: Literal["datetime"] = "datetime"
    required: bool = False
    default: datetime = Field(default_factory=dt_now)

    def receive(self, value: str | datetime | date | None = None) -> datetime:
        if value is None:
            return self.default

        if isinstance(value, datetime):
            return value
        elif isinstance(value, date):
            return datetime(value.year, value.month, value.day)
        elif not isinstance(value, str):
            raise ValueError(
                f"Value that want to convert to datetime does not support for "
                f"type: {type(value)}"
            )
        return datetime.fromisoformat(value)


class StrParams(DefaultParams):
    """String parameter."""

    type: Literal["str"] = "str"

    def receive(self, value: Optional[str] = None) -> str | None:
        if value is None:
            return self.default
        return str(value)


class IntParams(DefaultParams):
    """Integer parameter."""

    type: Literal["int"] = "int"

    def receive(self, value: Optional[int] = None) -> int | None:
        if value is None:
            return self.default
        if not isinstance(value, int):
            try:
                return int(str(value))
            except TypeError as err:
                raise ValueError(
                    f"Value that want to convert to integer does not support "
                    f"for type: {type(value)}"
                ) from err
        return value


class ChoiceParams(BaseParams):
    type: Literal["choice"] = "choice"
    options: list[str]

    def receive(self, value: Optional[str] = None) -> str:
        """Receive value that match with options."""
        # NOTE:
        #   Return the first value in options if does not pass any input value
        if value is None:
            return self.options[0]
        if any(value not in self.options):
            raise ValueError(f"{value} does not match any value in options")
        return value


Params = Union[
    ChoiceParams,
    DatetimeParams,
    StrParams,
]


class Pipeline(BaseModel):
    """Pipeline Model"""

    params: dict[str, Params] = Field(default_factory=dict)
    jobs: dict[str, Job]

    @classmethod
    def from_loader(
        cls,
        name: str,
        externals: Optional[DictData] = None,
    ) -> Self:
        loader: Loader = Loader(name, externals=(externals or {}))
        if "jobs" not in loader.data:
            raise ValueError("Config does not set ``jobs`` value")
        return cls(
            jobs=loader.data["jobs"],
            params=loader.data["params"],
        )

    def job(self, name: str) -> Job:
        """Return Job model that exists on this pipeline.

        :param name: A job name that want to get from a mapping of job models.
        :type name: str

        :rtype: Job
        """
        if name not in self.jobs:
            raise ValueError(f"Job {name} does not exists")
        return self.jobs[name]

    def execute(self, params: DictData | None = None) -> DictData:
        """Execute pipeline with passing dynamic parameters.

        See Also:

            The result of execution process for each jobs and stages on this
        pipeline will keeping in dict which able to catch out with all jobs and
        stages by dot annotation.

            For example, when I want to use the output from previous stage, I
        can access it with syntax:

            ... "<job-name>.stages.<stage-id>.outputs.<key>"

        """
        params: DictData = params or {}
        check_key = tuple(f"{k!r}" for k in self.params if k not in params)
        if check_key:
            raise ValueError(
                f"Parameters that needed on pipeline does not pass: "
                f"{', '.join(check_key)}."
            )

        if any(p not in params for p in self.params if self.params[p].required):
            raise ValueError("Required parameter does not pass")

        params: DictData = {
            "params": (
                params
                | {
                    k: self.params[k].receive(params[k])
                    for k in params
                    if k in self.params
                }
            )
        }
        for job_id in self.jobs:
            print(f"[PIPELINE]: Start execute the job: {job_id!r}")
            job: Job = self.jobs[job_id]
            # TODO: Condition on ``needs`` of this job was set. It should create
            #   multithreading process on this step.
            job.execute(params=params)
        return params
