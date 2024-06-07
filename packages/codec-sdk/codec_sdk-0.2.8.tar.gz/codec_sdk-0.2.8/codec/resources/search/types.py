from pydantic import BaseModel

class TargetSegments(BaseModel):
    previous: str
    target: str
    next: str


class SearchResult(BaseModel):
    video: str
    result_type: str
    score: float
    original_filename: str
    duration: int
    collection: dict
    video_url: str
    timestamp_start: int
    timestamp_end: int
    thumbnail_url: str
    target_segments: TargetSegments
