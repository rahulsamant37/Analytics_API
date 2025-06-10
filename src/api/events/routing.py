from fastapi import APIRouter
from .schema import EventSchema

router = APIRouter()

@router.get("/")
def read_events():
    """
    Endpoint to retrieve a list of events.
    """
    return {
        "results": [1,2,3]
    }

@router.get("/{event_id}")
def get_event(event_id: int)-> EventSchema:
    """
    Endpoint to retrieve a specific event by its ID.
    """
    return {"id": event_id}