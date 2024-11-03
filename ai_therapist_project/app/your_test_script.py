import requests
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OpenAI API key not found. Make sure it’s set in your .env file.")

# Set up headers and data for Chat Completion API
headers = {
    "Authorization": f"Bearer {OPENAI_API_KEY}",
    "Content-Type": "application/json",
}

# Use the messages parameter instead of prompt for Chat Completion API
data = {
    "model": "gpt-4o-mini",  # or "gpt-3.5-turbo" if using that model
    "messages": [
        {"role": "user", "content": "How are you doing?"}  # Replace with your input message
    ],
    "max_tokens": 100,
    "temperature": 0.4,
}

# Make the request to OpenAI's Chat Completion API
response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)

# Print the response
response_data = response.json()
ai_text = response_data.get("choices", [{}])[0].get("message", {}).get("content", "").strip()

print(ai_text)