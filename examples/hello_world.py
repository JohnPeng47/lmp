from pydantic import BaseModel

from lmp import LMP
from models import openai_41

class Answer(BaseModel):
    answer: str

class Ask(LMP):
    prompt = """
What is capital of {{country}}?
"""
    response_format = Answer

if __name__ == "__main__":
    res = Ask().invoke(
        model=openai_41(),
        prompt_args={"country": "France"}
    )
    print(res.answer)