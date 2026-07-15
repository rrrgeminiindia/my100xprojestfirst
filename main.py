import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from groq import Groq
from pydantic import BaseModel

load_dotenv()

app = FastAPI(
    title="Automation Diagnosis API",
    version="1.0.0",
)


class DiagnoseRequest(BaseModel):
    workflow_description: str


@app.get("/")
def home():
    return {
        "status": "running",
        "message": "Automation Diagnosis API is live",
    }


@app.get("/health")
def health():
    return {"status": "healthy"}


@app.post("/diagnose")
def diagnose(request: DiagnoseRequest):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY is not configured",
        )

    system_instruction = """
You are an expert Automation Architect and Business Analyst coaching a junior
analyst who is building their first automation.

Generate a detailed Automation Diagnosis Plan in professional Markdown with:

## Executive Summary
## Workflow Analysis
## Recommended Tech Stack
## Step-by-Step Implementation Blueprint
## Key Risks & Considerations
## Your First Action Item RIGHT NOW
"""

    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": system_instruction,
                },
                {
                    "role": "user",
                    "content": (
                        "Diagnose this workflow and generate an Automation "
                        f"Diagnosis Plan:\n\n{request.workflow_description}"
                    ),
                },
            ],
            temperature=0.4,
            max_tokens=4096,
        )

        return {
            "diagnosis": response.choices[0].message.content
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=f"Groq API error: {error}",
        ) from error
