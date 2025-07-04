from fastapi import FastAPI
from typing import Union
from api.events import router as events_router

app = FastAPI()
app.include_router(events_router, prefix="/api/events")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}

@app.get("items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
