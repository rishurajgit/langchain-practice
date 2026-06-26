from fastapi import APIRouter

from self_correcting_output_api.schema import (
    AnswerRequest,
    AnswerResponse,
)
from self_correcting_output_api.workflow import generate_answer


router = APIRouter(
    prefix="/answer",
    tags=["Self Correcting Answer"],
)


@router.post("/",response_model=AnswerResponse)
def answer(request: AnswerRequest):

    result = generate_answer(
        question=request.question
    )

    return AnswerResponse(
        answer=result
    )