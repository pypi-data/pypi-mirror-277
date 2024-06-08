from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Completion:
    """Represents the result of an auto complete search."""

    value: str
    type: str

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> Completion:
        return Completion(
            value=data["display"],
            type=data["type"],
        )
