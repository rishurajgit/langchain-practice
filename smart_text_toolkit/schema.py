from pydantic import BaseModel
from enum import Enum

class TransformAction(str, Enum):
    summarize = "summarize"
    translate = "translate"
    tone_shift = "tone-shift"
    
    
class TransformRequest(BaseModel):
    text: str
    action: TransformAction
    
class TransformResponse(BaseModel):
    result: str