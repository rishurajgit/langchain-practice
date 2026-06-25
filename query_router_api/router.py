from fastapi import APIRouter

from query_router_api.schema import QueryRequest, QueryResponse
from query_router_api.workflow import ask_question


router = APIRouter(
    prefix="/ask",
    tags=["Query Router API"]
)


@router.post("/",response_model=QueryResponse)
def ask(request: QueryRequest):

    result = ask_question(
        question=request.question
    )

    return QueryResponse(
        answer=result
    )