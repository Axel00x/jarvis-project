TOOL_DEFINITIONS = [
    {
        "name": "open_browser",
        "description": "Opens the browser on a specific URL. Use this when the user wants to visit a site, search on Google, open YouTube, etc.",
        "parameters": {
            "type": "object",
            "properties": {
                "url": {
                    "type": "string",
                    "description": "Full URL to open, e.g., https://youtube.com"
                }
            },
            "required": ["url"]
        }
    },
    {
        "name": "search_google",
        "description": "Searches for something on Google. Use this when the user wants information on a topic.",
        "parameters": {
            "type": "object",
            "properties": {
                "query": {
                    "type": "string",
                    "description": "Text to search on Google"
                }
            },
            "required": ["query"]
        }
    },
    {
        "name": "create_word_document",
        "description": "Creates a Word document with the provided text.",
        "parameters": {
            "type": "object",
            "properties": {
                "file_name": {
                    "type": "string",
                    "description": "File name without extension"
                },
                "content": {
                    "type": "string",
                    "description": "Text to insert into the document"
                }
            },
            "required": ["file_name", "content"]
        }
    },
    {
        "name": "open_application",
        "description": "Opens an application installed on the PC. E.g.: notepad, calc, spotify, discord.",
        "parameters": {
            "type": "object",
            "properties": {
                "app_name": {
                    "type": "string",
                    "description": "Name of the application to open"
                }
            },
            "required": ["app_name"]
        }
    },
    {
        "name": "get_weather",
        "description": "Returns the current weather for a city.",
        "parameters": {
            "type": "object",
            "properties": {
                "city": {
                    "type": "string",
                    "description": "Name of the city, e.g., Rome, Milan"
                }
            },
            "required": ["city"]
        }
    }
]   