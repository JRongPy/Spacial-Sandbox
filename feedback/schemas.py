from pydantic import BaseModel


class Feedback(BaseModel):
    data: dict
