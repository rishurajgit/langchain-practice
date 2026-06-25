from fastapi import APIRouter

from resume_parser.schema import ResumeRequest, ResumeData
from resume_parser.workflow import parse_resume


router = APIRouter(
    prefix="/parse-resume",
    tags=["Resume Parser"]
)


@router.post("/",response_model=ResumeData)
def parse(request: ResumeRequest):

    result = parse_resume(
        resume_text=request.resume_text
    )

    return result