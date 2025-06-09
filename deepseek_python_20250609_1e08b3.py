# main.py
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import httpx

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files (frontend)
app.mount("/", StaticFiles(directory="static", html=True), name="static")

LM_API_URL = "http://localhost:1234/v1/chat/completions"

@app.post("/generate")
async def generate(request: Request):
    body = await request.json()
    prompt = body.get("prompt", "")

    payload = {
        "model": "deepseek-coder",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7,
        "max_tokens": 1000
    }

    try:
        async with httpx.AsyncClient(timeout=60.0) as client:
            response = await client.post(LM_API_URL, json=payload)
            response.raise_for_status()
            data = response.json()
            
        ai_response = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        return {"response": ai_response}
    
    except Exception as e:
        return {"response": f"⚡ ERROR: {str(e)}"}