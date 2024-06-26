from __future__ import annotations
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Extra, Field, StrictStr


class ResetPassword(BaseModel):
    class Config:
        extra = Extra.forbid

    login: Optional[StrictStr] = Field(None, description='Login')
    email: Optional[StrictStr] = Field(None, description='Email')
