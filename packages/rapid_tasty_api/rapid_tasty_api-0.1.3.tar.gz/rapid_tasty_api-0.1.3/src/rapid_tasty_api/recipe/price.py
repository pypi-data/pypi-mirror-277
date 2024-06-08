from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime
from typing import Any


@dataclass(frozen=True, slots=True)
class Price:
    """Represents the price of a recipe in cents (probably USD)."""

    consumption_portion: int
    consumption_total: int
    portion: int
    total: int
    updated_at: datetime

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Price:
        return Price(
            consumption_portion=data["consumption_portion"],
            consumption_total=data["consumption_total"],
            portion=data["portion"],
            total=data["total"],
            updated_at=datetime.fromisoformat(data["updated_at"]),
        )
