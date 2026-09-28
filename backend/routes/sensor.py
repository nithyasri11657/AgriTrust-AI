from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter(
    prefix="/sensor",
    tags=["Sensor Data"]
)


class SensorData(BaseModel):
    temperature: float
    humidity: float
    soil_moisture: float
    soil_ph: float
    nitrogen: float
    phosphorus: float
    potassium: float


@router.post("/data")
def receive_sensor_data(data: SensorData):
    return {
        "success": True,
        "message": "Sensor data received successfully",
        "data": data.model_dump()
    }