from app.services.feedback_generator import custom_feedback_logic

def test_custom_feedback():
    result = custom_feedback_logic("Test submission", "clarity, accuracy")
    assert isinstance(result, str)
    assert "clarity" in result
