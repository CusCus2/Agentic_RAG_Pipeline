from fastapi import FastAPI
from pydantic import BaseModel
from rag_pipeline import build_rag_system, answer_query

app = FastAPI(title="Agentic RAG API")

class QueryRequest(BaseModel):
    query: str

class QueryResponse(BaseModel):
    query : str
    action: str
    answer: str
    sources: list[dict]

rag_setup = build_rag_system()

@app.get("/health")
def health():
    return {"status" : "ok"}

@app.post("/query", response_model=QueryResponse)
def query(request : QueryRequest):
    res = answer_query(
        query = request.query,
        retriever = rag_setup["retriever"],
        llm = rag_setup["llm"]
    )
    return res