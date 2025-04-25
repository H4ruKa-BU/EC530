if __name__ == "__main__":
    sample_text = """
    This paper explores how AI impacts classroom workflows and teaching responsibilities. It provides structured arguments and reflects critical thinking.
    """

    example_rubric = {
        "clarity": {
            "description": "How clearly are ideas and arguments expressed?",
            "weight": 0.3
        },
        "structure": {
            "description": "How well is the essay organized, with introduction, body, and conclusion?",
            "weight": 0.2
        },
        "originality": {
            "description": "How original or insightful are the points made?",
            "weight": 0.3
        },
        "evidence": {
            "description": "Are claims supported by examples or logical reasoning?",
            "weight": 0.2
        }
    }

    result = grade_with_rubric(sample_text, example_rubric)
    print(result["raw_response"])
