from app.services.llm_engine import analyze_document

def test_analysis_format():
    response = analyze_document("This is a sample answer", "Clarity, structure, originality")
    assert isinstance(response, dict)
    assert "grade" in response
    assert "feedback" in response
