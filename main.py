from fastapi import FastAPI
from openai import OpenAI
import os

app = FastAPI()

# Claves de API
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Cliente de OpenAI
client = OpenAI(api_key=OPENAI_API_KEY)

@app.get("/")
async def home():
    return {"message": "Kairo Virtual Assistant"}

@app.post("/ask")
async def ask_question(query: str):
    response = client.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": query}]
    )
    return {"response": response.choices[0].message["content"]}
