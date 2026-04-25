from langchain_core.prompts import PromptTemplate

extract_prompt = PromptTemplate(
    input_variables=["resume"],
    template="""
You are an AI system that extracts structured information from resumes.

TASK:
Extract ONLY the following fields from the resume:
- skills
- tools
- experience

STRICT RULES:
- Extract ONLY what is explicitly mentioned in the resume
- Do NOT infer, assume, or expand anything
- Do NOT normalize abbreviations (keep exactly as written)
- If a field is not present, return empty list or empty string
- Return ONLY valid JSON (no markdown, no explanation)
- Ensure JSON is properly formatted and parsable
- Extract candidate name if present

OUTPUT FORMAT (MANDATORY):

{{
  "candidate_name": "",
  "skills": [],
  "tools": [],
  "experience": ""
}}

IMPORTANT:
- "experience" must be exactly as written (e.g., "2 years", "6 months", "0 years")
- Do NOT add any extra fields
- Do NOT wrap output in text or backticks
- Do NOT include trailing commas

Resume:
{resume}
""".strip()
)