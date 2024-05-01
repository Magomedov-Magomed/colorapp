from drf_spectacular.openapi import OpenApiParameter
from pydantic import BaseModel


class BaseSchema(BaseModel):
    summary: str = ''
    description: str = ''


class ShowCasePhoneNumSchema(BaseSchema):
    parameters: list = [
        OpenApiParameter(
            name='number_type',
            type=str,
            enum=['abc', 'def', 'all'],
            location=OpenApiParameter.QUERY,
            description='Тип номеров. abc: стационарный; def: мобильный',
            default='all',
        ),
        OpenApiParameter(
            name='area_id',
            location=OpenApiParameter.QUERY,
            description='Area id',
            required=False,
            type=int,
        ),
    ]


class AreasSchema(BaseSchema):
    parameters: list = [
        OpenApiParameter(
            name='number_type',
            type=str,
            enum=['abc', 'def', 'all'],
            location=OpenApiParameter.QUERY,
            description='Тип номеров. abc: стационарный; def: мобильный',
            default='all',
        ),
    ]
