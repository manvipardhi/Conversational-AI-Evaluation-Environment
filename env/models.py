from pydantic import BaseModel

class Observation(BaseModel):
    query: str
    context: str = ""

class Action(BaseModel):
    response: str

class Reward(BaseModel):
    score: float
    feedback: str