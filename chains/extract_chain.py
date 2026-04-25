import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from prompts.extract_prompt import extract_prompt

# Load env safely
load_dotenv()

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=0,
    api_key=os.getenv("GROQ_API_KEY")
)

extract_chain = (
    extract_prompt
    | llm.with_config({"run_name": "Extract Step"})
    | StrOutputParser()
)