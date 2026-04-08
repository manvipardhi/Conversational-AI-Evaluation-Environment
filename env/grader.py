def grade_response(task, response):
    score = 0
    feedback = []

    # keyword check
    for word in task["expected_keywords"]:
        if word in response.lower():
            score += 0.3
            feedback.append(f"{word} found")

    # politeness
    if any(w in response.lower() for w in ["sorry", "please"]):
        score += 0.2
        feedback.append("Polite tone")

    # completeness
    if len(response.split()) > 8:
        score += 0.2
        feedback.append("Detailed response")

    return min(score, 1.0), ", ".join(feedback)