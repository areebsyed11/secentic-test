from typing import Literal
from pydantic import BaseModel, Field
from datetime import datetime
from .models import AgentStatus, RegistrationSource


class AgentRegisterRequest(BaseModel):
    name: str = Field(min_length=1, max_length=200, pattern=r"\S")
    owner: str | None = Field(default=None, max_length=200)
    environment: Literal["development", "staging", "production"] = "development"


class AgentResponse(BaseModel):
    id: str
    name: str
    owner: str | None
    environment: str
    status: AgentStatus
    registration_source: RegistrationSource
    first_seen: datetime
    last_seen: datetime

    class Config:
        from_attributes = True