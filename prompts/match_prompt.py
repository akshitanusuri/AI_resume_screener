
from langchain_core.prompts import PromptTemplate

match_prompt = PromptTemplate(
    input_variables=["resume_data", "job_description"],
    template="""
You are a strict skill matcher.

TASK:
Compare resume with job description.

STRICT RULES:
- Return ONLY valid JSON
- No explanation
- No markdown
- No text before or after JSON
- Do NOT use objects like {{ "skill": ... }}
- Use ONLY plain lists of strings

OUTPUT FORMAT (STRICT):
{{
  "matched_skills": [],
  "missing_skills": [],
  "preferred_matched": []
}}

LOGIC:
- matched_skills → REQUIRED skills present in resume
- missing_skills → REQUIRED skills NOT present
- preferred_matched → PREFERRED skills present

Resume:
{resume_data}

Job Description:
{job_description}
"""
)