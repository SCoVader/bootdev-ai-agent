import os
import sys
from dotenv import load_dotenv
from google import genai
from functions.config import *
from functions.get_files_info import get_files_info
from functions.get_files_info import schema_get_files_info


available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)

def show_usage():
    print("Boot.dev ai agent")
    print("\nUsage: main \"your question or request\" [--verbose]")
    pass

def main(*args, **kwargs):
    messages = ""

    if len(args[0]) < 2: 
        show_usage()
        return 1
    
    messages = str(args[0][1])

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=genai.types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )

    print(response.text)
    
    if "--verbose" in args[0] or "-V" in args[0]:
        print("User prompt: ", messages)
        print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print("Response tokens: ",  response.usage_metadata.candidates_token_count)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
