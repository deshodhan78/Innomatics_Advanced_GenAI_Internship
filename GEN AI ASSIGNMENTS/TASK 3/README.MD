# AI-Powered Resume Screening System

An intelligent **AI-based resume screening tool** that automatically evaluates candidates by comparing their resumes with a given job description. Built using **LangChain**, **Groq**, and **LangSmith**.

---

## ✨ Features

* **Automated Skill Extraction** from resumes (skills, experience, tools, education)
* **Intelligent Matching** against job requirements
* **Fit Score Calculation** (0–100)
* **Explainable AI** – Detailed reasoning for every score
* **Structured JSON Output** using Pydantic
* **Modular LangChain Pipeline** with LCEL (LangChain Expression Language)
* **Tracing & Debugging** support with LangSmith
* **Fast Inference** using Groq (Llama-3.3-70B)

---

## 📊 Sample Results

| Candidate         | Fit Score  | Status    |
| ----------------- | ---------- | --------- |
| Strong Candidate  | **92/100** | Excellent |
| Average Candidate | **60/100** | Average   |
| Weak Candidate    | **10/100** | Poor      |

---

## 🛠️ Tech Stack

* **Python 3**
* **LangChain** (LCEL)
* **Groq** (`llama-3.3-70b-versatile`)
* **Pydantic** (Structured Output)
* **LangSmith** (Tracing & Monitoring)
* **dotenv** (Environment Variables)

---

## 📁 Project Structure

```
ai-resume-screening-system/
├── main.py                     # Main entry point
├── models.py                   # Pydantic data models
├── prompts/
│   ├── extraction_prompt.py    # Prompt for skill extraction
│   └── scoring_prompt.py       # Prompt for matching & scoring
├── chains/
│   ├── extraction_chain.py     # Extraction chain
│   └── scoring_chain.py        # Scoring chain
├── .env                        # Environment variables (not pushed)
├── .gitignore
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/ai-resume-screening-system.git
cd ai-resume-screening-system
```

### 2. Install Dependencies

```bash
pip install langchain langchain-groq pydantic python-dotenv
```

### 3. Setup Environment Variables

Create a `.env` file in the root directory:

```env
# Groq API Key (Required)
GROQ_API_KEY=gsk_your_groq_api_key_here

# LangSmith Tracing (Optional)
LANGSMITH_TRACING=true
LANGSMITH_API_KEY=lsv2_your_langsmith_api_key
LANGSMITH_PROJECT=resume-screening-system
```

> Get Groq API Key: https://console.groq.com/keys

### 4. Run the Project

```bash
python main.py
```

---

## 📝 Key Learnings

* Building end-to-end LLM pipelines using **LangChain Expression Language (LCEL)**
* Prompt engineering for reliable structured outputs
* Handling structured output challenges with Groq using `json_mode`
* Tracing and debugging LLM applications with **LangSmith**
* Creating explainable AI systems for HR/recruitment use cases

---

## 🔧 Challenges & Solutions

* **Challenge**: Structured output failures (400 error) on Groq
  **Solution**: Switched to `method="json_mode"` in `with_structured_output()`

* **Challenge**: LangSmith 403 Forbidden errors
  **Solution**: Properly configured project and API key

---

## 🎯 Assignment Requirements Fulfilled

* ✅ AI-powered Resume Screening System
* ✅ Modular pipeline using LangChain
* ✅ Skill extraction + matching + scoring + explanation
* ✅ Use of PromptTemplate and LCEL
* ✅ Structured output with Pydantic
* ✅ LangSmith integration for tracing
* ✅ Explainable AI outputs

---

## 🚀 Future Enhancements

* PDF resume parsing support
* Few-shot prompting for better accuracy
* Web interface using Streamlit
* Batch processing of multiple resumes
* Candidate ranking dashboard

---

**Built as part of Generative AI Assignment**

Made with ❤️ using LangChain & Groq
