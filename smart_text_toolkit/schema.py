from pydantic import BaseModel
from enum import Enum

class ActionType(str, Enum):
    summarize = "summarize"
    translate = "translate"
    tone_shift = "tone_shift"
    
    
class TransformRequest(BaseModel):
    text: str
    action: str
    
class TransformResponse(BaseModel):
    result: str