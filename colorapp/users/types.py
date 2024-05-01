from typing import TypedDict


class UserCreateData(TypedDict):
    username: str
    name: str
    password: str
