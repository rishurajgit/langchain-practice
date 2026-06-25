from pathlib import Path

from langchain_core.prompts import PromptTemplate

from common.llm import llm
from resume_parser.schema import ResumeData


# Prompt Folder

PROMPTS_FOLDER = Path(__file__).parent / "prompts"



# Load Prompt

def load_prompt(file_name: str) -> str:

    file_path = PROMPTS_FOLDER / file_name

    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


# Prompt Template


resume_prompt = PromptTemplate.from_template(
    load_prompt("parse_resume.txt")
)


# Structured LLM

structured_llm = llm.with_structured_output(
    ResumeData
)

# Chain

resume_chain = (
    resume_prompt
    | structured_llm
)


# Main Function

def parse_resume(resume_text: str) -> ResumeData:

    result = resume_chain.invoke(
        {
            "resume_text": resume_text
        }
    )

    return result