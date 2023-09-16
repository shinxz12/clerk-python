from typing import List, Optional, Union
from pydantic import BaseModel


class ResponseError(BaseModel):
    errors: List[dict]
    status_code: int
    meta: Optional[dict] = None

    @property
    def is_success(self) -> False:
        ...


class ResponseSuccess(BaseModel):
    data: Union[dict, List[dict]]
    status_code: int

    @property
    def is_success(self) -> True:
        ...


class RetrieveResponseSuccess(ResponseSuccess):
    data: dict


class ListResponseSuccess(ResponseSuccess):
    data: List[dict]


Response = Union[ResponseError, Union[RetrieveResponseSuccess, ListResponseSuccess]]
RetrieveResponse = Union[ResponseError, RetrieveResponseSuccess]
ListResponse = Union[ResponseError, ListResponseSuccess]
