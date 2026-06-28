import webbrowser
import subprocess
import requests
from docx import Document

def open_browser(url: str) -> str:
    try:
        webbrowser.open(url)
        return f"Browser opened on {url}"
    except Exception as e:
        return f"Error: {e}"

def search_google(query: str) -> str:
    url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
    webbrowser.open(url)
    return f"Google search opened for: '{query}'"

def create_word_document(file_name: str, content: str) -> str:
    try:
        doc = Document()
        doc.add_paragraph(content)
        path = f"{file_name}.docx"
        doc.save(path)
        return f"Document '{path}' created"
    except Exception as e:
        return f"Document creation error: {e}"

def open_application(app_name: str) -> str:
    # Map common names to system commands
    APP_MAP = {
        "notepad":  "notepad.exe",
        "calculator": "calc.exe",
        "file explorer": "explorer.exe",
        "spotify":  "spotify",
        "discord":  "discord",
        "chrome":   "chrome",
        "vscode":   "code",
    }
    
    command = APP_MAP.get(app_name.lower(), app_name)
    
    try:
        subprocess.Popen(command)
        return f"Application '{app_name}' opened"
    except FileNotFoundError:
        return f"Application '{app_name}' not found"

def get_weather(city: str) -> str:
    try:
        # wttr.in is free, no API key required
        url = f"https://wttr.in/{city}?format=3&lang=en"
        response = requests.get(url, timeout=5)
        return response.text.strip()
    except Exception as e:
        return f"Unable to get weather: {e}"


# Dictionary mapping name to function (used by the dispatcher)
TOOL_MAP = {
    "open_browser":        open_browser,
    "search_google":       search_google,
    "create_word_document": create_word_document,
    "open_application":    open_application,
    "get_weather":         get_weather,
}   