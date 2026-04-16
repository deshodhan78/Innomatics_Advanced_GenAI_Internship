from pydantic import BaseModel, Field
from typing import List

class ExtractedInfo(BaseModel):
    """Step 1: Structured skill/experience extraction"""
    skills: List[str] = Field(description="Only skills EXPLICITLY mentioned in the resume. Do not assume or add any.")
    experience_years: int = Field(description="Number of years of relevant professional experience. Use 0 if not mentioned.")
    tools: List[str] = Field(description="Tools, frameworks, libraries mentioned.")
    education: str = Field(description="Highest degree or education level mentioned.")

class ScreeningResult(BaseModel):
    """Final output: Match + Score + Explanation"""
    matched_skills: List[str]
    missing_skills: List[str]
    fit_score: int = Field(ge=0, le=100, description="Overall fit score 0-100")
    explanation: str = Field(description="Clear, concise reasoning for the score. Reference specific matches/mismatches.")