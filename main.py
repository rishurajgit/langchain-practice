from fastapi import FastAPI

from health.router import router as health_router
from smart_text_toolkit.router import router as smart_text_router

app = FastAPI()

app.include_router(health_router)
app.include_router(smart_text_router)