from pydantic import BaseModel

class GeneratePostRequest(BaseModel):
    topic: str
    
    
class GeneratePostResponse(BaseModel):
    tweet: str
    linkedin_caption: str
    hastag: str