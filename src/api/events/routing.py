from fastapi import APIRouter
from .schema import (
    EventSchema, 
    EventListSchema, 
    EventCreateSchema, 
    EventUpdateSchema
)

router = APIRouter()

@router.get("/")
def read_events() -> EventListSchema:
    """
    Endpoint to retrieve a list of events.
    """
    return {
        "results": [
            {"id": 1},
            {"id": 2},
            {"id": 3}
        ]
    }

@router.post("/")
def create_event(payload:EventCreateSchema) -> EventSchema:
    """
    Endpoint to create a new event.
    """
    print(payload.page)
    return {"id": 123}

@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    """
    Endpoint to retrieve a specific event by its ID.
    """
    return {"id": event_id}

@router.put("/{event_id}")
def update_event(event_id: int, payload:EventUpdateSchema) -> EventSchema:
    """
    Endpoint to update an existing event by its ID.
    """
    print(payload.description)
    return {"id": event_id}
