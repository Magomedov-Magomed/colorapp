from pydantic import BaseModel


class BaseSchema(BaseModel):
    summary: str = ''
    description: str = ''
