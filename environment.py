from env.tasks import get_task
from env.grader import grade_response

class CustomerSupportEnv:

    def __init__(self):
        self.task = None
        self.done = False

    def reset(self):
        self.task = get_task()
        self.done = False
        return self.task["query"]

    def step(self, action):
        score, feedback = grade_response(self.task, action)
        self.done = True
        return "Task Completed", score, self.done, {"feedback": feedback}

    def state(self):
        return self.task