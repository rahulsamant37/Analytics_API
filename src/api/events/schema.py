from typing import List, Optional
from pydantic import BaseModel, Field

class EventCreateSchema(BaseModel):
    page: str
    description: Optional[str] = Field(default="")

class EventUpdateSchema(BaseModel):
    description: str

class EventSchema(BaseModel):
    id: int
    page: Optional[str] = ""
    description: Optional[str] = ""


class EventListSchema(BaseModel):
    results: List[EventSchema]