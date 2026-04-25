import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from prompts.explain_prompt import explain_prompt

# Load environment variables safely
load_dotenv()

# Explicit API key 
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

explain_chain = (
    explain_prompt
    | llm.with_config({"run_name": "Explain Step"})
    | StrOutputParser()
)