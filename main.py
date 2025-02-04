from fastapi import FastAPI, HTTPException
from datetime import date, datetime
from pydantic import BaseModel, Field
from fastapi.staticfiles import StaticFiles

app=FastAPI()

class HeatPump(BaseModel):
    name: str
    serial_num: float = Field(gt=0)
    install_date: date


app.heat_pump = HeatPump(
    name = "default",
    serial_num=1,
    install_date=date(2000, 1, 1)
)

@app.get("/heat_pump")
def get_heat_pump() ->HeatPump:
    if app.heat_pump is None:
        raise HTTPException(404, "Not found pump")
    return app.heat_pump


@app.put("/heat_pump")
def put_heat_pump(pump: HeatPump):
    app.heat_pump = pump


app.mount(
    "/", StaticFiles(directory=".", html=True)
)