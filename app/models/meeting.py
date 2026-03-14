from pydantic import BaseModel

class MeetingRequest(BaseModel):
    transcript: str


class MeetingResponse(BaseModel):
    summary: str
    tasks: list[str]
    deadlines: list[str]
    decisions: list[str]