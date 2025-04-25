from pydantic import BaseModel

class FeedbackResponse(BaseModel):
    grade: int
    feedback: str
