from fastapi import APIRouter
from app.models.meeting import MeetingRequest
from app.services.meeting_service import analyze_meeting


router = APIRouter()

@router.post("/meeting/analyze")
def analyze_meeting_api(request: MeetingRequest):
    result = analyze_meeting(request.transcript)
    return result