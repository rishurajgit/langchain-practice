from pathlib import Path

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

from common.llm import llm


# Prompt Folder

PROMPTS_FOLDER = Path(__file__).parent / "prompts"


# Load Prompt
def load_prompt(file_name: str) -> str:

    file_path = PROMPTS_FOLDER / file_name

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# Prompt Templates
answer_prompt = PromptTemplate.from_template(
    load_prompt("answer.txt")
)

review_prompt = PromptTemplate.from_template(
    load_prompt("review.txt")
)

rewrite_prompt = PromptTemplate.from_template(
    load_prompt("rewrite.txt")
)


# Chains
answer_chain = (
    answer_prompt
    | llm
    | StrOutputParser()
)

review_chain = (
    review_prompt
    | llm
    | StrOutputParser()
)

rewrite_chain = (
    rewrite_prompt
    | llm
    | StrOutputParser()
)


# Main Workflow
def generate_answer(question: str) -> str:

    # Step 1 : Generate  answer
    answer = answer_chain.invoke(
        {
            "question": question
        }
    )

    # Step 2 : Review the answer
    review = review_chain.invoke(
        {
            "question": question,
            "answer": answer,
        }
    )

    # Step 3 : If answer is GOOD
    if review.strip().upper() == "GOOD":
        return answer

    # Step 4 : Rewrite the answer
    improved_answer = rewrite_chain.invoke(
        {
            "question": question,
            "answer": answer,
        }
    )

    return improved_answer