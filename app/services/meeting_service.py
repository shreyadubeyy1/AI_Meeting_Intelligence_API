def analyze_meeting(transcript: str):

    sentences = transcript.split(".")
    sentences = [s.strip() for s in sentences if s.strip()]

    summary = sentences[:2]

    return {
        "summary": " ".join(summary),
        "tasks": ["Finish UI", "Prepare presentation"],
        "deadlines": ["Friday"],
        "decisions": ["Launch next month"]
    }