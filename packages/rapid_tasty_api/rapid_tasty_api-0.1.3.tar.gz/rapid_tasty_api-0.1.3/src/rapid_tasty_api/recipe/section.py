from __future__ import annotations

from dataclasses import dataclass
from typing import Any

from .component import Component


@dataclass(frozen=True, slots=True)
class Section:
    """Represents a part of a recipe."""

    components: list[Component]
    name: str | None
    position: int

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Section:
        return Section(
            components=[
                Component.from_dict(component) for component in data["components"]
            ],
            name=data["name"],
            position=data["position"],
        )
