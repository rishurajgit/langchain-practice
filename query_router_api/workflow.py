from pathlib import Path

from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnableLambda

from common.llm import llm


# Prompt Folder

PROMPTS_FOLDER = Path(__file__).parent / "prompts"


# Load Prompt

def load_prompt(file_name: str) -> str:

    file_path = PROMPTS_FOLDER / file_name

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# Prompt Templates

classification_prompt = PromptTemplate.from_template(
    load_prompt("classify.txt")
)

coding_prompt = PromptTemplate.from_template(
    load_prompt("coding.txt")
)

math_prompt = PromptTemplate.from_template(
    load_prompt("math.txt")
)

general_prompt = PromptTemplate.from_template(
    load_prompt("general.txt")
)

# Classifier Chain

classifier_chain = (
    classification_prompt
    | llm
    | StrOutputParser()
)


# Expert Chains

coding_chain = (
    coding_prompt
    | llm
    | StrOutputParser()
)

math_chain = (
    math_prompt
    | llm
    | StrOutputParser()
)

general_chain = (
    general_prompt
    | llm
    | StrOutputParser()
)


# Helper Function

def classify_question(data):

    category = classifier_chain.invoke(
        {
            "question": data["question"]
        }
    )

    return {
        "question": data["question"],
        "category": category.strip().lower()
    }


# Runnable Branch

workflow = (

    RunnableLambda(classify_question)
    
    |

    RunnableBranch(

        (
            lambda data: data["category"] == "coding",
            coding_chain,
        ),

        (
            lambda data: data["category"] == "math",
            math_chain,
        ),

        general_chain
    )

)


# Main Function

def ask_question(question: str) -> str:

    result = workflow.invoke(
        {
            "question": question
        }
    )

    return (result)