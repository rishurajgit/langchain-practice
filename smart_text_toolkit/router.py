from fastapi import APIRouter

from smart_text_toolkit.schema import TransformRequest,TransformResponse
from smart_text_toolkit.workflow import transform_text


router = APIRouter(
    prefix="/transform",
    tags=["Smart Text Toolkit"],
)


@router.post("/",response_model=TransformResponse)
def transform(request: TransformRequest):

    result = transform_text(
        text=request.text,
        action=request.action,
    )

    return TransformResponse(
        result=result
    )