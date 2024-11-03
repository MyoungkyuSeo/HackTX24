from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.schema.runnable import RunnableSequence
import requests
import os
from safetycheck import models  # Import the function from safety_check.py

# app = FastAPI() 

# Load environment variables from .env file
load_dotenv()

# # Get the OpenAI API key from environment variables
# OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# if not OPENAI_API_KEY:
#     raise ValueError("OPENAI_API_KEY environment variable not set")

# class ScrapedTextRequest(BaseModel):
#     text: str

chain = models()

msg = chain.invoke("So great! Good job!")

print(msg)

# @app.post("/process-text")
# async def process_text(scraped_text_request: ScrapedTextRequest):
#     scraped_text = scraped_text_request.text
#     headers = {
#         "Authorization": f"Bearer {OPENAI_API_KEY}",
#         "Content-Type": "application/json",
#     }
#     data = {
#         "model": "gpt-4o-mini",
#         "messages": [
#             {"role": "user", "content": template},
#             {"role": "user", "content": "I am lonely, I want to end it all."}
#         ],
#         "max_tokens": 100,
#         "temperature": 0.4,
#     }

#     try:
#         # Step 1: Make the initial OpenAI API call
#         response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
#         response.raise_for_status()

#         # Step 2: Extract the assistant's response content
#         response_data = response.json()
#         print(response_data)
#         ai_text = response_data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()

#         # Step 3: Run the safety check on the AI-generated text
#         final = ai_text
        
#         # Step 4: If harmful content is detected, return the corrective action; otherwise, return ai_text
#         print(final)
#         return final
       
#     except requests.exceptions.RequestException as e:
#         raise HTTPException(status_code=500, detail=f"Error communicating with OpenAI API: {e}")

