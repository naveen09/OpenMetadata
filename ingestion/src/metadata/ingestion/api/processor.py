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
from typing import Any, List

from .closeable import Closeable
from .common import Record, WorkflowContext
from .status import Status


@dataclass
class ProcessorStatus(Status):
    records = 0
    warnings: List[Any] = field(default_factory=list)
    failures: List[Any] = field(default_factory=list)

    def processed(self, record: Record):
        self.records += 1

    def warning(self, info: Any) -> None:
        self.warnings.append(info)

    def failure(self, info: Any) -> None:
        self.failures.append(info)


@dataclass
class Processor(Closeable, metaclass=ABCMeta):
    ctx: WorkflowContext

    @classmethod
    @abstractmethod
    def create(
        cls, config_dict: dict, metadata_config_dict: dict, ctx: WorkflowContext
    ) -> "Processor":
        pass

    @abstractmethod
    def process(self, record: Record) -> Record:
        pass

    @abstractmethod
    def get_status(self) -> ProcessorStatus:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
