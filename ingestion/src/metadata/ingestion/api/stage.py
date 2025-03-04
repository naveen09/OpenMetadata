#  Licensed to the Apache Software Foundation (ASF) under one or more
#  contributor license agreements. See the NOTICE file distributed with
#  this work for additional information regarding copyright ownership.
#  The ASF licenses this file to You under the Apache License, Version 2.0
#  (the "License"); you may not use this file except in compliance with
#  the License. You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from abc import ABCMeta, abstractmethod
from dataclasses import dataclass, field
from typing import Dict, List, TypeVar

from .closeable import Closeable
from .common import Record, WorkflowContext
from .status import Status


@dataclass
class StageStatus(Status):
    records_produced = 0

    warnings: Dict[str, List[str]] = field(default_factory=dict)
    failures: Dict[str, List[str]] = field(default_factory=dict)

    def records_status(self, record: Record) -> None:
        self.records_produced += 1

    def warning_status(self, key: str, reason: str) -> None:
        if key not in self.warnings:
            self.warnings[key] = []
        self.warnings[key].append(reason)

    def failure_status(self, key: str, reason: str) -> None:
        if key not in self.failures:
            self.failures[key] = []
        self.failures[key].append(reason)


RecordType = TypeVar("RecordType", bound=Record)


@dataclass  # type: ignore[misc]
class Stage(Closeable, metaclass=ABCMeta):
    ctx: WorkflowContext

    @classmethod
    @abstractmethod
    def create(
        cls, config_dict: dict, metadata_config_dict: dict, ctx: WorkflowContext
    ) -> "Stage":
        pass

    @abstractmethod
    def stage_record(self, record: Record):
        pass

    @abstractmethod
    def get_status(self) -> StageStatus:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
