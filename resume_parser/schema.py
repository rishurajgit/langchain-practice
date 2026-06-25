from pydantic import BaseModel

# Request Model

class ResumeRequest(BaseModel):
    resume_text: str


# Structured Resume Model

class ResumeData(BaseModel):
    name: str
    skills: list[str]
    years_of_experience: int
    last_role: str