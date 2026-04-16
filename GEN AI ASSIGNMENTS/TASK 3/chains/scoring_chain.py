from langchain_groq import ChatGroq
from prompts.scoring_prompt import SCORING_PROMPT
from models import ScreeningResult

def create_scoring_chain(llm):
    # Use json_mode for better reliability on Groq
    structured_llm = llm.with_structured_output(
        ScreeningResult,
        method="json_mode"          # ← This is the key fix
    )
    
    return (
        SCORING_PROMPT
        | structured_llm
    )