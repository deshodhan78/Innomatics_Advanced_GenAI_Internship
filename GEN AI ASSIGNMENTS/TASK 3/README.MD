# AI-Powered Resume Screening System

## Overview
An intelligent resume screening tool that uses **Large Language Models (LLMs)** to automatically evaluate candidates by comparing their resumes against a given job description. The system extracts key information, matches skills, assigns a fit score (0-100), and provides clear explanations.

This project demonstrates a complete **LLM-based evaluation pipeline** using LangChain, Groq, and LangSmith.

## Features
- **Skill & Experience Extraction** from resumes
- **Automated Matching** with job requirements
- **Fit Score Calculation** (0-100)
- **Explainable AI** – Detailed reasoning for every score
- **Modular LangChain Pipeline** using LCEL
- **Structured JSON Output** using Pydantic
- **Tracing & Debugging** with LangSmith
- **Fast Inference** using Groq (Llama-3.3-70B)

## Tech Stack
- **Python**
- **LangChain** (LCEL)
- **Groq** (`llama-3.3-70b-versatile`)
- **Pydantic** (Structured Output)
- **LangSmith** (Tracing & Monitoring)
- **dotenv** (Environment Management)

## Project Structure