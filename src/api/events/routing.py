from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_events():
    """
    Endpoint to retrieve a list of events.
    """
    return {
        "items": [1,2,3]
    }