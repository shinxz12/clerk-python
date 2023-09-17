from typing import Literal, List, Optional
from pydantic import BaseModel
from .session import Session


class Client(BaseModel):
    object: Literal["client"]
    id: str
    session_ids: List[str]
    sessions: List[Session]
    sign_in_id: Optional[str]
    sign_up_id: Optional[str]
    last_active_session_id: Optional[str]
    updated_at: int
    created_at: int
