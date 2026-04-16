from langchain_groq import ChatGroq
from prompts.extraction_prompt import EXTRACTION_PROMPT
from models import ExtractedInfo

def create_extraction_chain(llm):
    structured_llm = llm.with_structured_output(
        ExtractedInfo,
        method="json_mode"
    )
    
    return (
        EXTRACTION_PROMPT
        | structured_llm
    )