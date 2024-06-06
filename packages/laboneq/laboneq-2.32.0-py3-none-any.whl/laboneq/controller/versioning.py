# Copyright 2022 Zurich Instruments AG
# SPDX-License-Identifier: Apache-2.0

from __future__ import annotations

from enum import Enum
from functools import total_ordering

import laboneq


@total_ordering
class LabOneVersion(Enum):
    UNKNOWN = "0"
    V_24_01 = "24.01"
    V_24_04 = "24.04"
    LATEST = V_24_04

    def __eq__(self, other):
        return float(self.value) == float(other.value)

    def __lt__(self, other):
        return float(self.value) < float(other.value)

    @classmethod
    def cast(cls, version: str, raise_if_unsupported: bool = True) -> LabOneVersion:
        try:
            labone_version = LabOneVersion(version)
        except ValueError as e:
            if raise_if_unsupported:
                err_msg = (
                    f"LabOne version {version} is not supported by LabOne Q {laboneq.__version__}."
                    f" Please downgrade/upgrade your LabOne installation, instruments'"
                    f" firmware and API to version {cls.LATEST.value}."
                )
                raise ValueError(err_msg) from e
            else:
                labone_version = LabOneVersion.UNKNOWN
        return labone_version


class SetupCaps:
    def __init__(self, version: LabOneVersion):
        self._version = version

    @property
    def result_logger_pipelined(self) -> bool:
        return True

    @property
    def flexible_feedback(self) -> bool:
        return False
