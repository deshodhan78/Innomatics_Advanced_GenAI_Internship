from langchain_core.prompts import PromptTemplate

EXTRACTION_PROMPT = PromptTemplate.from_template(
    """You are an expert HR data extractor.
Extract ONLY information that is EXPLICITLY present in the resume.
Do NOT assume or hallucinate any skills, tools, or experience.

Resume:
{resume}

Return a valid JSON object matching this schema:
- skills: list of technical skills
- experience_years: integer (0 if not mentioned)
- tools: list of tools/frameworks
- education: string

Strict rule: If a skill/tool is not written in the resume, do NOT include it.
"""
)