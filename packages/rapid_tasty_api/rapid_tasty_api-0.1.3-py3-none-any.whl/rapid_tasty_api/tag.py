from __future__ import annotations

from dataclasses import dataclass
from io import StringIO
from typing import Any


@dataclass(frozen=True, slots=True)
class Tag:
    """Represents a tag of a recipe."""

    id: int
    type: str
    name: str
    display_name: str

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Tag:
        return Tag(
            id=data["id"],
            type=data["type"],
            name=data["name"],
            display_name=data["display_name"],
        )


def tag_list_to_str(tags: list[Tag]) -> str:
    """
    Helper function to turn a list of Tag objects into a TastyAPI compatible string. Used when filtering requests by tags.

    :param list[Tag] tags: The list of Tag objects.
    :return str: A formatted string containing all the tags, ready for use in an requests.
    """

    buffer = StringIO()

    for i, tag in enumerate(tags):
        buffer.write(tag.name)
        if i != len(tags) - 1:
            buffer.write(",")

    ret = buffer.getvalue()
    buffer.close()

    return ret
