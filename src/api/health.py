from fastapi import APIRouter
import time
from src.retrieval.vector_store import vector_store

router = APIRouter(prefix="/health", tags=["Health"])

START_TIME = time.time()

@router.get("")
def health():
    return {
        "status": "healthy",
        "indexed_vectors": vector_store.index.ntotal if vector_store else 0,
        "uptime_seconds": round(time.time() - START_TIME, 2)
    }
