from fastapi import FastAPI
from datetime import datetime
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles

app=FastAPI()

class HeatPump(BaseModel):
    name: str
    serial_num: int
    install_date: datetime


app.heat_pump = HeatPump(
    name = "default",
    serial_num=1,
    install_date=datetime(2000, 1, 1)
)

@app.get("/heat_pump")
def get_heat_pump() ->HeatPump:
    return app.heat_pump

@app.put("/heat_pump")
def put_heat_pump(pump: HeatPump):
    app.heat_pump = pump

app.mount(
    "/", StaticFiles(directory=".", html=True)
)