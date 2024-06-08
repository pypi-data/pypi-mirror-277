from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class Instruction:
    """Represents a single step in the recipe's instructions."""

    appliance: str | None
    display_text: str
    end_time: int
    id: int
    position: int
    start_time: int
    # TODO (when I find an example): temperature: SOMETHING | None

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Instruction:
        return Instruction(
            appliance=data["appliance"],
            display_text=data["display_text"],
            end_time=data["end_time"],
            id=data["id"],
            position=data["position"],
            start_time=data["start_time"],
        )
