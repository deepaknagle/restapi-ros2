from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

travel_data = {}

class Travel(BaseModel):
    travel_id: int
    travel_name: str
    parameters: Optional[dict] = None

@app.post("/travel")
def post_mission(travel: Travel):
    travel_data[travel.travel_id] = travel
    return{"status": "Trip received"}

@app.get("/travel/{travel_id}")
def get_mission(travel_id: int):
    travel = travel_data.get(travel_id)
    if travel:
        return travel
    else:
        return {"error": "Trip not found"}