# Copyright 2024 - GitHub user: fredericks1982

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This module contains the classes for the CAME Domotic status updates.

from dataclasses import dataclass
from typing import List

from .base import CameEntity


@dataclass
class CameUpdates(CameEntity):
    """List of status updates from the CameDomotic API."""

    _raw_data: dict

    @property
    def _updates_by_cmd_name(self) -> dict:
        """List of status updates grouped by cmd_name."""
        updates = self._raw_data.get("result", [])
        updates_by_cmd_name: dict[str, List[dict]] = {}
        for item in updates:
            cmd_name = item.get("cmd_name")
            if cmd_name not in updates_by_cmd_name:
                updates_by_cmd_name[cmd_name] = []
            updates_by_cmd_name[cmd_name].append(item)
        return updates_by_cmd_name

    @property
    def light_updates(self) -> dict[str, dict]:
        """List of light status updates."""
        result: dict[str, dict] = {}
        for item in self._updates_by_cmd_name.get("light_switch_ind", []):
            act_id = item.get("act_id")
            if act_id:
                result[act_id] = item
        return result
