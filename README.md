# 🤖 Automation Diagnosis Tool

A CLI tool powered by **Gemini 2.5 Flash** that takes a plain-English description of a manual workflow and generates a structured **Automation Diagnosis Plan** — perfect for an analyst building their first automation.

---

## ⚡ Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add your Gemini API key

Open `.env` and paste your key:

```
GEMINI_API_KEY=your_actual_key_here
```

> Get a **free** key at: https://aistudio.google.com/app/apikey

### 3. Run the tool

**Interactive mode** (recommended for students):

```bash
python main.py
```

You'll be prompted to type or paste your workflow description. Press **Enter twice** when done.

**Quick mode** (pass workflow as argument):

```bash
python main.py "Every Monday I download a sales CSV from our ERP, copy the totals into a Google Sheet, and email a summary to my manager."
```

---

## 📋 What You Get

The tool outputs a structured **Automation Diagnosis Plan** with:

| Section | What It Contains |
|---|---|
| 🔍 Executive Summary | Quick overview of what the automation will do |
| 🗂️ Workflow Analysis | Triggers, inputs, steps, and outputs |
| 🛠️ Recommended Tech Stack | Best tools for this specific use case + why |
| 🚀 Implementation Blueprint | Phase 1 MVP → Phase 2 → Phase 3 |
| ⚠️ Risks & Considerations | Edge cases, security, rate limits |
| ✅ First Action Item | One task to start RIGHT NOW |

---

## 🧠 How It Works

```
Your workflow description (text)
        ↓
  diagnose() function
        ↓
  Gemini 2.5 Flash API
  (system prompt as Automation Architect)
        ↓
  Structured Markdown Diagnosis Plan
```

The `diagnose(workflow_description: str) -> str` function can also be imported and used in other scripts:

```python
from main import diagnose

plan = diagnose("Every week I manually copy invoices from email into a spreadsheet...")
print(plan)
```

---

## 📁 Project Structure

```
.
├── main.py           # Core diagnose() function + CLI
├── requirements.txt  # Python dependencies
├── .env              # Your API keys (never commit this!)
└── README.md         # This file
```
