from typing import Generic, Optional, TypeVar
from pydantic.generics import GenericModel


T = TypeVar("T")

class ResponseSchema(GenericModel, Generic[T]):
    status: int
    message: str
    data: Optional[T] = None

    model_config = {
        "arbitrary_types_allowed": True,
        "populate_by_name": True,
        "from_attributes": True
    }