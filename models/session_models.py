from typing import Literal, Optional
from pydantic import BaseModel


class Session(BaseModel):
    object: Literal["session"]
    id: str
    client_id: str
    user_id: str
    status: str
    actor: Optional[str]
    last_active_at: int
    expire_at: int
    abandon_at: int
    created_at: int
    updated_at: int
