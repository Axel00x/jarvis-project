# Librerie chiave per ogni funzionalità

## Input vocale / output voce

- `SpeechRecognition` + `PyAudio` — riconoscimento vocale (Google STT gratuito)
- `edge-tts` — voce sintetica di alta qualità (voci Microsoft, gratis)
- `pyttsx3` — TTS offline, più semplice ma qualità inferiore
- `faster-whisper` — STT locale molto accurato (OpenAI Whisper ottimizzato)

## Automazione del PC

- `pyautogui` — controlla mouse, tastiera, screenshot
- `subprocess` — apre programmi, esegue comandi di sistema
- `keyboard` / `pynput` — hotkey globali (es. tieni premuto un tasto per parlare)
- `pygetwindow` — gestisce le finestre aperte

## Web e informazioni

- `webbrowser` — apre URL nel browser
- `requests` / `httpx` — chiamate HTTP
- `beautifulsoup4` — scraping web
- `newsapi-python` — notizie (API gratuita disponibile)
- `googlesearch-python` — ricerche Google

## File e applicazioni

- `python-docx` — crea/modifica Word
- `openpyxl` — Excel
- `os` / `pathlib` — gestione file system
- `pyperclip` — copia/incolla negli appunti

## AI e orchestrazione

- `openai` (SDK, funziona anche con Groq/Ollama) — chiamate LLM
- `langchain` — orchestrazione avanzata, memoria, tool calling
- `chromadb` — memoria vettoriale (per ricordare conversazioni passate)
