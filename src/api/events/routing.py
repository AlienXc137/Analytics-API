from fastapi import APIRouter

router=APIRouter()
# "/api/events"
@router.get("/")
def read_root():
    return {"items": [1,2,3]}