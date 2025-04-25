from fastapi import APIRouter
from pydantic import BaseModel
from app.services.llm_engine import analyze_document

router = APIRouter()

class AnalyzeRequest(BaseModel):
    student_id: str
    document_text: str
    rubric_id: str

@router.post("/analyze")
def analyze(request: AnalyzeRequest):
    result = analyze_document(request.document_text, request.rubric_id)
    return result
