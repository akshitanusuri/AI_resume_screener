import json
import re
from dotenv import load_dotenv
from langsmith import traceable

from chains.extract_chain import extract_chain
from chains.match_chain import match_chain
from chains.score_chain import score_chain
from chains.explain_chain import explain_chain

load_dotenv()


# UTILITIES 
def read_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


import re
import json

def safe_load(data, step):
    try:
        json_match = re.search(r'\{.*\}', data, re.DOTALL)
        if json_match:
            return json.loads(json_match.group())
        else:
            raise ValueError("No JSON found")
    except Exception as e:
        print(f"\n⚠️ JSON ERROR in {step}: {e}")
        print(data)
        return {}


#  DECISION LOGIC
def get_decision(score):
    if score >= 75:
        return "STRONG CANDIDATE"
    elif score >= 45:
        return "AVERAGE CANDIDATE"
    else:
        return "WEAK CANDIDATE"


#  PIPELINE 

@traceable(name="Resume Screening Pipeline")
def run_pipeline(resume_path, job_description_path):

    resume = read_file(resume_path)
    job_description = read_file(job_description_path)

    # STEP 1: EXTRACT
    print("\nSTEP 1: Extracting...")

    extracted_raw = extract_chain.invoke({"resume": resume})
    extracted = safe_load(extracted_raw, "EXTRACTION")

    print(json.dumps(extracted, indent=2))

    # STEP 2: MATCH 
    print("\nSTEP 2: Matching...")

    matched_raw = match_chain.invoke({
        "resume_data": json.dumps(extracted),   
        "job_description": job_description
    })

    matched = safe_load(matched_raw, "MATCHING")

    print("\nMATCH OUTPUT:")
    print(json.dumps(matched, indent=2))

    #  STEP 3: SCORE
    print("\nSTEP 3: Scoring...")

    scored_raw = score_chain.invoke({
        "match_data": json.dumps(matched),   
        "experience_years": extracted.get("experience", "0")
    })

    scored = safe_load(scored_raw, "SCORING")

    print(json.dumps(scored, indent=2))

    total_score = scored.get("total_score", 0)
    decision = get_decision(total_score)

    print(f"\nFINAL DECISION (SYSTEM): {decision}")

    # STEP 4: EXPLANATION
    print("\nSTEP 4: Explanation...")
    explained = ""
    explained = explain_chain.invoke({
        "candidate_name": extracted.get("candidate_name", "Unknown"),
        "total_score": total_score,
        "match_data": matched,    
        "final_decision": decision
    })

    

    print("\n" + "=" * 50)
    print(explained)
    print("=" * 50)

    return {
        "extracted": extracted,
        "matched": matched,
        "scored": scored,
        "decision": decision,
        "explained": explained
    }


# RUN

if __name__ == "__main__":

    print("\nSTRONG CANDIDATE")
    run_pipeline("data/resume_strong.txt", "data/job_description.txt")

    print("\nAVERAGE CANDIDATE")
    run_pipeline("data/resume_avg.txt", "data/job_description.txt")

    print("\nWEAK CANDIDATE")
    run_pipeline("data/resume_weak.txt", "data/job_description.txt")