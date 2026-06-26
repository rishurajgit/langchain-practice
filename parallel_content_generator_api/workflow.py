from pathlib import Path
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableParallel, RunnablePassthrough
from common.llm import llm



prompts_folder = Path(__file__).parent/"prompts"

# Load Prompt
def load_prompt(file_name: str) ->str:
    file_path = prompts_folder / file_name
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
tweet_prompt = PromptTemplate.from_template(
    load_prompt("tweet.txt")
)

linkedin_prompt = PromptTemplate.from_template(
    load_prompt("linkedin.txt")
)

hastag_prompt = PromptTemplate.from_template(
    load_prompt("hastag.txt")
)


# Chains
tweet_chain = (
    tweet_prompt
    | llm
    | StrOutputParser()
)

linkedin_chain = (
    linkedin_prompt
    | llm
    | StrOutputParser()
)

hastag_chain = (
    hastag_prompt
    | llm
    | StrOutputParser()
)


# Parallel Workflow

workflow = (

    RunnablePassthrough()

    |

    RunnableParallel(

        tweet=tweet_chain,

        linkedin_caption=linkedin_chain,

        hastag=hastag_chain,
    )

)


# Main Function
def generate_post(topic: str):

    result = workflow.invoke(
        {
            "topic": topic
        }
    )

    return result