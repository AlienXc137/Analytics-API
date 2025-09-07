from fastapi import APIRouter
from .schemas import EventSchema, EventListSchema, EventCreateSchema, EventUpdateSchema

router=APIRouter()
# "/api/events"
@router.get("/") 
def read_events() -> EventListSchema:
    return {"results": [{'id':1},{'id':2},{'id':3}]} # return a bunch of items

@router.post("/") 
def create_event(payload: EventCreateSchema) -> EventSchema:
    print(payload.page)
    return {"id":123}


@router.get("/{event_id}")
def get_event(event_id: int)  -> EventSchema:
    return {"id" : event_id}

@router.put("/{event_id}")
def get_event(event_id: int, payload:EventUpdateSchema)  -> EventSchema:
    print(payload.description)
    return {"id" : event_id}