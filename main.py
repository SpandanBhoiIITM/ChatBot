from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
import requests
import json

app=FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to your frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

OPENROUTER_API_KEY ="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"
@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_message = body.get("message")

    response = requests.post(
        url="https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json",
            "HTTP-Referer": "http://localhost:3000",  # or your live frontend URL
            "X-Title": "My Chatbot",},
            data=json.dumps({
            "model": "google/gemma-3n-e4b-it:free",
            "messages": [
                {
                    "role": "user",
                    "content": user_message
                }
            ],
        })
    )

    return response.json()