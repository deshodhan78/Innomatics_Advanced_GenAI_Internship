from dotenv import load_dotenv
import os

load_dotenv()

# Debug API Key
print("🔍 Checking GROQ_API_KEY...")
if os.getenv("GROQ_API_KEY"):
    print("✅ GROQ_API_KEY loaded successfully!")
else:
    print("❌ GROQ_API_KEY not found! Please check your .env file.")
    exit()

from chains.extraction_chain import create_extraction_chain
from chains.scoring_chain import create_scoring_chain
from models import ExtractedInfo
from langchain_groq import ChatGroq

# ====================== LLM Configuration (Groq) ======================
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=1024,
)

# Create chains using the new functions
extraction_chain = create_extraction_chain(llm)
scoring_chain = create_scoring_chain(llm)

# ====================== SAMPLE DATA ======================
JOB_DESCRIPTION = """We are looking for a Data Scientist with:
- Strong proficiency in Python and SQL
- Experience with Machine Learning frameworks (Scikit-learn, TensorFlow/PyTorch)
- Data visualization tools (Tableau, Power BI, Matplotlib)
- At least 3 years of relevant experience
- Cloud platforms (AWS, GCP or Azure) is a big plus
- Strong statistics and problem-solving skills"""

RESUMES = {
    "Strong Candidate": """Alice Johnson
5+ years as Data Scientist at TechCorp.
Skills: Python, SQL, Machine Learning, Scikit-learn, TensorFlow, PyTorch, Tableau, AWS, Statistics.
Education: MS Data Science, Stanford.
Built predictive models that increased revenue 25%.""",

    "Average Candidate": """Bob Smith
2 years as Data Analyst at StartupX.
Skills: Python, SQL, basic Machine Learning, Scikit-learn, Tableau.
Education: BS Statistics.
Analyzed sales data and created dashboards.""",

    "Weak Candidate": """Carol Lee
1 year internship in marketing analytics.
Skills: Excel, basic Python.
Education: BA Marketing.
No machine learning or SQL experience."""
}

# ====================== PIPELINE ======================
def screen_candidate(resume_text: str, candidate_name: str):
    print(f"\n{'='*70}")
    print(f"SCREENING: {candidate_name}")
    print(f"{'='*70}")

    # Step 1: Skill Extraction
    print("→ Step 1: Extracting skills/experience...")
    try:
        extracted = extraction_chain.invoke({"resume": resume_text})
        print("   ✅ Extraction successful")
        print("   Extracted:", extracted.model_dump_json(indent=2))
    except Exception as e:
        print(f"   ❌ Extraction failed: {e}")
        return

    # Step 2-4: Matching + Scoring + Explanation
    print("→ Step 2-4: Matching, Scoring & Explanation...")
    try:
        result = scoring_chain.invoke({
            "job_description": JOB_DESCRIPTION,
            "extracted_info": extracted.model_dump_json(indent=None)
        })

        print(f"   🎯 FIT SCORE: {result.fit_score}/100")
        print("\n   📝 Explanation:")
        print(result.explanation)
        print("\n   ✅ Matched Skills :", result.matched_skills)
        print("   ❌ Missing Skills:", result.missing_skills)

    except Exception as e:
        print(f"   ❌ Scoring failed: {e}")

if __name__ == "__main__":
    print("🚀 Resume Screening System Started with Groq (llama-3.3-70b-versatile)\n")
    
    for name, resume in RESUMES.items():
        screen_candidate(resume, name)

    print("\n" + "="*70)
    print("✅ All 3 candidates processed!")
    print("📊 View traces in LangSmith (if enabled): https://smith.langchain.com")
    print("="*70)