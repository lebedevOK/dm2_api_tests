from __future__ import annotations
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Extra, Field, StrictStr


class GeneralError(BaseModel):
    class Config:
        extra = Extra.forbid

    message: Optional[StrictStr] = Field(None, description='Client message')
