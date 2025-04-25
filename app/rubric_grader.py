import openai
from typing import Dict, List, Any

# Define a rubric grading system
def grade_with_rubric(submission_text: str, rubric: Dict[str, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Grades a submission using multiple rubric criteria with weightings.
    
    Args:
        submission_text: The text of the student's submission.
        rubric: A dictionary with keys as criteria (e.g., 'clarity') and values as dicts
                containing 'description' (what to evaluate) and 'weight' (importance).
    
    Returns:
        A dictionary with detailed score breakdown, total score, and feedback.
    """

    prompt_parts = [
        "You are an educational assistant tasked with grading a student essay based on the following criteria:\n"
    ]
    
    for key, val in rubric.items():
        prompt_parts.append(f"- {key.capitalize()} ({val['weight']}): {val['description']}\n")
    
    prompt_parts.append("\nNow evaluate the following student submission and assign a score (0-100) for each criterion, then compute a weighted average score:\n")
    prompt_parts.append(f"\n--- STUDENT SUBMISSION ---\n{submission_text}\n\n")
    prompt_parts.append("Return result in JSON format like:\n{\n  \"clarity\": {\"score\": 90, \"comment\": \"Well-written...\"},\n  ...\n  \"total_score\": 87,\n  \"summary_feedback\": \"...\"\n}\n")

    prompt = "".join(prompt_parts)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    
    # In production, wrap below with try/except and JSON validation
    parsed_result = response['choices'][0]['message']['content']
    
    # Optional: use json.loads(parsed_result) after sanitizing the response
    return {"raw_response": parsed_result}
