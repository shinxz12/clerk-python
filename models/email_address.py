from typing import List, Literal, Optional
from pydantic import BaseModel


class Verification(BaseModel):
    status: str
    strategy: str
    attempts: Optional[int]
    expire_at: Optional[int]


class LinkTo(BaseModel):
    type: str
    id: str


class EmailAddress(BaseModel):
    id: str
    object: Literal["email_address"]
    email_address: str
    reserved: bool
    verification: Optional[Verification] = None
    linked_to: List[Optional[LinkTo]]
