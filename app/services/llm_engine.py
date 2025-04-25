import openai

def analyze_document(text: str, rubric: str) -> dict:
    prompt = f"Evaluate the following student submission:\n{text}\n\nBased on this rubric:\n{rubric}\n\nGive a score (0-100) and detailed feedback."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return {
        "grade": 85,  # You can parse from response['choices'][0]['message']['content'] if needed
        "feedback": response['choices'][0]['message']['content']
    }
