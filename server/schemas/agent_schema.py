from typing import Optional
from uuid import UUID
from pydantic import BaseModel


class AgentCreate(BaseModel):
    hostname: Optional[str]
    os: Optional[str]

class AgentResponse(BaseModel):
    id: UUID
    hostname: Optional[str]
    os: Optional[str]

    class Config:
        orm_mode=True

class AgentUpdate(BaseModel):
    ostname: Optional[str]
    os: Optional[str]