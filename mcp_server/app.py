from fastmcp import FastMCP
from pydantic import BaseModel
import random
import json

app = FastMCP("mindmate-mcp")

# Load prompts JSON
with open("data/prompts.json", "r", encoding="utf-8") as f:
    prompts_data = json.load(f)

# Pydantic model
class UserEmotion(BaseModel):
    emotion: str

@app.tool()
def getMotivationalQuote(input_data: UserEmotion) -> dict:
    emotion = input_data.emotion.lower()
    matches = [p for p in prompts_data if p["emotion"].lower() == emotion]

    if not matches:
        return {"quote": f"I couldn't find a quote for '{emotion}', but remember: you’ve got this!"}

    return {"quote": random.choice(matches)["quote"]}

if __name__ == "__main__":
    app.run()   # ❗ STDIO üzerinden çalışır, Uvicorn yok
