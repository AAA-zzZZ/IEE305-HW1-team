from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel

app=FastAPI()

heat_pump=None

class HeatPump(BaseModel):
    name: str
    serial_num: int
    install_date: datetime


@app.get("/heat_pump")
def get_heat_pump():
    return heat_pump

@app.put("/heat_pump")
def put_heat_pump(pump: HeatPump):
    global heat_pump
    heat_pump = pump