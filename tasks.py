import random

tasks = [
    {
        "difficulty": "easy",
        "query": "Where is my order?",
        "expected_keywords": ["track", "order", "status"]
    },
    {
        "difficulty": "medium",
        "query": "I received wrong product",
        "expected_keywords": ["return", "refund", "replace"]
    },
    {
        "difficulty": "hard",
        "query": "Payment deducted but no order placed",
        "expected_keywords": ["refund", "sorry", "support"]
    }
]

def get_task():
    return random.choice(tasks)