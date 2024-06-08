from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Topic:
    """Represents a topics of the recipe."""

    name: str
    slug: str

    @classmethod
    def from_dict(cls, data: dict[str, str]) -> Topic:
        return Topic(name=data["name"], slug=data["slug"])
