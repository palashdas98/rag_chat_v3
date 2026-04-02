
{
  "filename": "Basic_Automobile_Engineering.pdf",
  "text_chunks": 820,
  "table_chunks": 96,
  "image_chunks": 112,
  "processing_time_seconds": 42.3
}

from fastapi import APIRouter, UploadFile
import time
from src.ingestion.pdf_parser import parse_pdf
from src.ingestion.embedder import embed_chunks
from src.retrieval.vector_store import add_to_index

router = APIRouter(prefix="/ingest", tags=["Ingestion"])

@router.post("")
async def ingest_pdf(file: UploadFile):
    start = time.time()

    text_chunks, table_chunks, image_chunks = parse_pdf(await file.read())

    all_chunks = text_chunks + table_chunks + image_chunks
    embeddings, metadatas = embed_chunks(all_chunks)

    add_to_index(embeddings, all_chunks, metadatas)

    return {
        "filename": file.filename,
        "text_chunks": len(text_chunks),
        "table_chunks": len(table_chunks),
        "image_chunks": len(image_chunks),
        "processing_time_sec": round(time.time() - start, 2)
    }