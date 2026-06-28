from google import genai
from google.genai import types
from skills import TOOL_DEFINITIONS, TOOL_MAP

client = genai.Client()

# Converti le definizioni nel formato che vuole Gemini
def _convert_tool(definition: dict):
    return types.Tool(
        function_declarations=[
            types.FunctionDeclaration(
                name=definition["name"],
                description=definition["description"],
                parameters=types.Schema(
                    type=types.Type.OBJECT,
                    properties={
                        k: types.Schema(
                            type=types.Type.STRING,
                            description=v["description"]
                        )
                        for k, v in definition["parameters"]["properties"].items()
                    },
                    required=definition["parameters"].get("required", [])
                )
            )
        ]
    )

GEMINI_TOOLS = [_convert_tool(t) for t in TOOL_DEFINITIONS]

# Modello con tool
tools_config = types.GenerateContentConfig(
    tools=GEMINI_TOOLS,
    system_instruction=(
        "Sei Jarvis, un assistente AI che controlla il PC dell'utente. "
        "Quando l'utente ti chiede di fare qualcosa, usa i tool disponibili. "
        "Rispondi sempre in italiano e molto brevemente."
    )
)

chat = client.chats.create(
    model="gemini-3.1-flash-lite",
    config=tools_config
)

def ex_tool(name: str, args: dict):
    func = TOOL_MAP.get(name)
    if not func:
        return f"Tool '{name}' not found"
    try:
        return func(**args)
    except Exception as e:
        return f"Error in '{name}': {e}"

def call_gemini_api(msg: str):

    response = chat.send_message(msg)

    while True:
        # Check if Gemini has requested any tool calls
        tool_calls = response.function_calls
        
        if not tool_calls:
            break
        
        # execute each tool call and collect results
        results = []
        for fc in tool_calls:
            name = fc.name
            args = dict(fc.args)
            
            print(f"Execute tool: {name}({args})")
            res = ex_tool(name, args)
            print(f"res: {res}")
            
            results.append(
                types.Part(
                    function_response=types.FunctionResponse(
                        name=name,
                        response={"result": res}
                    )
                )
            )
        
        response = chat.send_message(results)
    
    return response.text.strip() if response.text else ""