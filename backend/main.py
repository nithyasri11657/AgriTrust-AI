from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.routes import disease, sensor


app = FastAPI(
    title="AgriTrust AI",
    description="AI-powered Smart Agriculture Platform",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(disease.router)
app.include_router(sensor.router)


@app.get("/")
def root():
    return {
        "message": "AgriTrust AI Backend is running!"
    }