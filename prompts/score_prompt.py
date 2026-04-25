from langchain_core.prompts import PromptTemplate

score_prompt = PromptTemplate(
    input_variables=["match_data", "experience_years"],
    template="""
You are an expert AI recruiter scoring system used in ATS (Applicant Tracking Systems).

TASK:
Calculate a FINAL candidate score between 0 and 100 based on job relevance.

IMPORTANT RULES:
- Return ONLY valid JSON
- Do NOT include explanation, text, or reasoning
- Do NOT hallucinate or assume missing skills
- Be deterministic and consistent

SCORING GUIDELINES:

1. SKILL MATCHING (70 points total):
- Count total_required = matched_skills + missing_skills
- skill_score = (number of matched_skills / total_required) * 70
- If total_required = 0, skill_score = 0

2. PREFERRED SKILLS BONUS (Max 10 points):
- Each preferred_matched skill adds +2 points
- bonus_score = min(len(preferred_matched) * 2, 10)

3. EXPERIENCE SCORING (30 points total):
- 4+ years → 30
- 2–3 years → 20
- 1 year or less → 10
- No experience → 0

4. FINAL RULE:
- total_score = skill_score + bonus_score + experience_score
- Ensure score is an integer between 0 and 100 (round if needed)

OUTPUT FORMAT (STRICT):

{{
  "total_score": <integer>
}}

INPUT:

Match Data:
{match_data}

Experience:
{experience_years}
"""
)