from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class Ratings:
    count_negative: int
    count_positive: int
    score: float

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Ratings:
        return Ratings(
            count_negative=data["count_negative"],
            count_positive=data["count_positive"],
            score=data["score"],
        )
