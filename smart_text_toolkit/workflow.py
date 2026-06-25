from pathlib import Path
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch
from common.llm import llm
from smart_text_toolkit.schema import TransformAction


prompts_folder = Path(__file__).parent / "prompts"

# Load Prompt

def load_prompt(file_name: str) -> str:
    file_path = prompts_folder / file_name
    
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()
    
    
# Prompt Templates

summarize_prompt = PromptTemplate.from_template(
    load_prompt("summarize.txt")
)

translate_prompt = PromptTemplate.from_template(
    load_prompt("translate.txt")
)

tone_shift_prompt = PromptTemplate.from_template(
    load_prompt("tone_shift.txt")
)


# Chains

summarize_chain = (
    summarize_prompt
    | llm
    | StrOutputParser()
)

translate_chain = (
    translate_prompt
    | llm
    | StrOutputParser
)

tone_shift_chain = (
    tone_shift_prompt
    | llm
    | StrOutputParser
)

workflow = RunnableBranch(
    (
        lambda data: data["action"] == TransformAction.summarize,
        summarize_chain,
    ),
    (
        lambda data: data["action"] == TransformAction.translate,
        translate_chain,
    ),
    (
        lambda data: data["action"] == TransformAction.tone_shift,
        tone_shift_chain,
    ),
)

# Main Function

def transform_text(text: str, action: TransformAction) -> str:
    
    result = workflow.invoke(
        {
            "text": text,
            "action": action,
        }
    )

    return result