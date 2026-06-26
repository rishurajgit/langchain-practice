from fastapi import APIRouter
from parallel_content_generator_api.schema import GeneratePostRequest, GeneratePostResponse
from parallel_content_generator_api.workflow import generate_post

router = APIRouter(
    prefix="/parallel-generate-post",
    tags=["Parallel Content Generator"]
)

@router.post("/",response_model=GeneratePostResponse)
def generate(request: GeneratePostRequest):
    result = generate_post(topic=request.topic)
    
    return GeneratePostResponse(
        tweet = result["tweet"],
        linkedin_caption = result["linkedin_caption"],
        hastag = result["hastag"]
    )
    