from fastapi import FastAPI, Request
from pydantic import BaseModel
from app.rag_pipeline import RAGPipeline

app = FastAPI()

rag = RAGPipeline()

class Query(BaseModel):
    question: str

@app.post("/query")
async def query_rag(query: Query):
    answer = rag.answer_question(query.question)
    return {"answer": answer}

@app.get("/")
async def root():
    return {"message": "Multilingual RAG System (Bangla + English)"}
