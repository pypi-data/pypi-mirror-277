from typing import Any
from pydantic import BaseModel, ConfigDict

from .generators import AbstractBaseGenerator


class TableConfig(BaseModel):
    name: str
    row_count: int = 1_000


class FieldConfig(BaseModel):
    model_config = ConfigDict(extra="allow")

    name: str
    dtype: Any
    # TODO: This is bad
    generator: AbstractBaseGenerator.__class__.__class__


class FieldMetadata(BaseModel):
    dtype: type
    position: int
