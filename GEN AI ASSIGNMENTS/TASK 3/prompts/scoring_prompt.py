from langchain_core.prompts import PromptTemplate

SCORING_PROMPT = PromptTemplate.from_template(
    """You are an expert recruiter for a Data Scientist role.

Job Description:
{job_description}

Candidate extracted profile:
{extracted_info}

Compare the candidate ONLY against the job description.
- Match skills/tools that appear in both
- Identify missing critical requirements
- Calculate a fit_score (0-100) based on:
   • Required technical skills (weight 50%)
   • Experience level (weight 30%)
   • Tools & education (weight 20%)

Output ONLY a valid JSON with this exact structure:
{{
  "matched_skills": [...],
  "missing_skills": [...],
  "fit_score": <integer 0-100>,
  "explanation": "Clear bullet-point style reasoning why this score was given. Be specific."
}}

Do NOT add any extra text outside the JSON.
"""
)