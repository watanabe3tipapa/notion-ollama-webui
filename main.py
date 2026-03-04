"""Notion + Ollama Web UI"""
import os
from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import requests
from ollama import chat
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Notion + Ollama Web UI")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

NOTION_KEY = os.getenv("NOTION_API_KEY")

def get_notion_page(page_id: str) -> dict:
    """Notion APIでページを取得"""
    url = f"https://api.notion.com/v1/pages/{page_id}"
    headers = {
        "Authorization": f"Bearer {NOTION_KEY}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    return requests.get(url, headers=headers).json()

def extract_text(page_data: dict) -> str:
    """ページからテキストを抽出"""
    props = page_data.get("properties", {})
    for key, prop in props.items():
        if prop.get("type") == "title":
            title_list = prop.get("title", [])
            return "".join([t.get("plain_text", "") for t in title_list])
    return ""

def ask_ollama(text: str, prompt: str) -> str:
    """Ollamaで回答生成"""
    full_prompt = f"{prompt}\n\n内容: {text}"
    response = chat('llama3.2', messages=[
        {"role": "user", "content": full_prompt}
    ])
    return response['message']['content']

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
async def ask(
    page_id: str = Form(...),
    prompt: str = Form(...)
):
    if not NOTION_KEY:
        return {"error": "NOTION_API_KEYが設定されていません"}
    
    page_data = get_notion_page(page_id)
    if "error" in page_data:
        return {"error": page_data.get("error", "エラーが発生しました")}
    
    text = extract_text(page_data)
    if not text:
        return {"error": "テキストが取得できませんでした"}
    
    result = ask_ollama(text, prompt)
    return {"result": result, "title": text[:50]}
