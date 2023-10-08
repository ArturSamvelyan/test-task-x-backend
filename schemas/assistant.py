from pydantic import BaseModel


class QuestionSchema(BaseModel):
    api_token: str
    question: str
