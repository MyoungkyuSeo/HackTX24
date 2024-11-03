from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
import requests 
import os

app = FastAPI() 

# Load environment variables from .env file
load_dotenv()

# Get the OpenAI API key from environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set")

class ScrapedTextRequest(BaseModel):
    text: str

@app.post("/process-text")
async def process_text(scraped_text_request: ScrapedTextRequest):
    scraped_text = scraped_text_request.text
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": "gpt-4o-mini",  # Set to "gpt-4-turbo" or "gpt-3.5-turbo"
        "messages": [
            {"role": "user", "content": scraped_text}
        ],
        "max_tokens": 100,
        "temperature": 0.4,
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()

        # Attempt to extract only the assistant's response content
        response_data = response.json()
        ai_text = response_data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()
       
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Error communicating with OpenAI API: {e}")
    

    return {"processed_text": ai_text}