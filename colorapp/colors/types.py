from typing import NotRequired, TypedDict


class ColorData(TypedDict):
    palette_id: int
    hex: str
    name: NotRequired[str]
