from fastapi import FastAPI
from src.api.health import router as health_router
from src.api.ingest import router as ingest_router
from src.api.query import router as query_router
import time

app = FastAPI(
    title="Multimodal Automobile Engineering RAG",
    description="Text, Table & Image-aware RAG System for Automobile Engineering",
    version="1.0.0"
)

app.include_router(health_router)
app.include_router(ingest_router)
app.include_router(query_router)

START_TIME = time.time()

@app.get("/")
def root():
    return {"message": "Automobile Multimodal RAG System is running"}
