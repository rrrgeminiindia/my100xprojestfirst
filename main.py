import os

from fastapi import FastAPI, HTTPException
from groq import Groq
from pydantic import BaseModel

app = FastAPI()


class DiagnoseRequest(BaseModel):
    workflow_description: str


@app.get("/")
def home():
    return {"status": "running"}


@app.post("/diagnose")
def diagnose(request: DiagnoseRequest):
    api_key = os.getenv("GROQ_API_KEY")

    if not api_key:
        raise HTTPException(
            status_code=500,
            detail="GROQ_API_KEY is not configured",
        )

    try:
        client = Groq(api_key=api_key)

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": "You are an expert automation architect.",
                },
                {
                    "role": "user",
                    "content": request.workflow_description,
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
            detail=str(error),
        ) from error
