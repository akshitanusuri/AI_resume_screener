# 🎯 AI Resume Screening System

A production-level AI pipeline that screens resumes against job descriptions using **LangChain**, **Groq (Llama 3.3-70B)**, and **LangSmith** for full observability.

> **Zero cost system** — built entirely on free-tier APIs. No OpenAI key required.

---

## ✨ Features

- **4-Step LLM Pipeline** → Extract → Match → Score → Explain  
- **Weighted Scoring System** → Skills (50%) + Experience (30%) + Tools (20%)  
- **Explainable AI Decisions** → Every score backed with evidence  
- **LangSmith Tracing** → Full visibility into each pipeline step  
- **Streamlit UI** → Simple recruiter dashboard  
- **Debug Mode** → Intentional flawed prompt to test hallucinations  

---

## 🏗️ Architecture

```text
resume_screener/
|
├── prompts/
|   ├── extraction_prompt.py        # Extract skills, tools, experience
|   ├── matching_prompt.py          # Compare JD vs Resume
|   ├── scoring_prompt.py           # Generate weighted score (0-100)
|   └── explanation_prompt.py       # Final hiring decision
|
├── chains/
|   ├── llm_factory.py              # Groq LLM setup
|   ├── extraction_chain.py         # Step 1 pipeline
|   ├── matching_chain.py           # Step 2 pipeline
|   ├── scoring_chain.py            # Step 3 pipeline
|   └── explanation_chain.py        # Step 4 pipeline
|
├── data/
|   ├── job_description.txt
|   ├── resume_strong.txt
|   ├── resume_average.txt
|   └── resume_weak.txt
|
├── main.py                         # CLI execution pipeline
├── app.py                          # Streamlit UI
├── requirements.txt
└── .env.example
```
```

---

## 🔄 Pipeline Flow

```text
Resume Input
    │
    ▼
[Step 1] Extraction
→ skills, tools, experience (JSON output)

    │
    ▼
[Step 2] Matching
→ matched vs missing skills/tools

    │
    ▼
[Step 3] Scoring
→ weighted score (0–100) + grade (A–F)

    │
    ▼
[Step 4] Explanation
→ final hiring recommendation

    │
    ▼
LangSmith Tracing (full observability)
```

---

## 🚀 Quickstart

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/ai-resume-screener
cd ai-resume-screener
pip install -r requirements.txt
```

---

### 2️⃣ Get API keys

- Groq → https://console.groq.com/
- LangSmith → https://smith.langchain.com/

---

### 3️⃣ Setup environment

```bash
cp .env.example .env
```

Fill in:

```env
GROQ_API_KEY=your_groq_key
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=your_langsmith_key
LANGCHAIN_PROJECT=ai-resume-screener
```

---

### 4️⃣ Run CLI pipeline

```bash
python main.py
```

Runs:
- Strong candidate
- Average candidate
- Weak candidate
- Debug hallucination test

---

### 5️⃣ Run Streamlit UI

```bash
streamlit run app.py
```

---

## 📊 Scoring System

| Component     | Weight |
|---------------|--------|
| Skills        | 50%    |
| Experience    | 30%    |
| Tools         | 20%    |

---

## 🏁 Grade System

| Grade | Score Range |
|------|-------------|
| A    | 85–100      |
| B    | 70–84       |
| C    | 50–69       |
| D    | 30–49       |
| F    | 0–29        |

---

## 🔍 LangSmith Observability

Every run is fully traceable:

- Prompt inputs & outputs
- Latency per chain
- Token usage
- Step-by-step debugging
- Hallucination detection (debug mode)

---

## 🧠 Tech Stack

- **LLM** → Groq (Llama 3.3-70B)
- **Framework** → LangChain (LCEL)
- **Tracing** → LangSmith
- **UI** → Streamlit
- **Language** → Python 3.10+

---

## 🧪 Debug Mode

A special mode intentionally uses a flawed prompt to:

- Trigger hallucinated outputs  
- Show LLM weaknesses  
- Validate LangSmith tracing effectiveness  

---

## 📌 Why This Project Matters

This project demonstrates:

- Real-world LLM pipeline design  
- Multi-step reasoning systems  
- Explainable AI decision-making  
- Prompt engineering + debugging  
- Production-level LangChain architecture  

---

## 📜 License

MIT License — free to use, modify, and extend.
