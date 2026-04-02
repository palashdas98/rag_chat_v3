Request:
{
  "question": "Explain hydraulic braking system"
}
Response:

{
  "answer": "The hydraulic braking system operates on Pascal’s law...",
  "sources": [
    {
      "page": 95,
      "chunk_type": "text"
    },
    {
      "page": 110,
      "chunk_type": "image_summary"
    }

from fastapi import APIRouter
from pydantic import BaseModel
from src.retrieval.rag_chain import run_rag

router = APIRouter(prefix="/query", tags=["Query"])

class QueryRequest(BaseModel):
    question: str

@router.post("")
def query_rag(request: QueryRequest):
    answer, sources = run_rag(request.question)
    return {"answer": answer, "sources": sources}
``