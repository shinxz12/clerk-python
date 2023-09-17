from typing import Any, Literal, Optional
from pydantic import BaseModel


class Session(BaseModel):
    object: Literal["session"]
    id: str
    user_id: str
    client_id: str
    actor: Optional[dict[Any, Any]]
    status: str
    last_active_organization_id: Optional[str] = None
    last_active_at: int
    expire_at: int
    abandon_at: int
    updated_at: int
    created_at: int
