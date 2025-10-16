import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from call_function import available_functions

from functions.config import *



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
        config=types.GenerateContentConfig(tools=[available_functions], system_instruction=system_prompt),
    )

    

    if not response.function_calls:
        print(response.text)
    else:
        function_call_part = response.function_calls[0]
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    
    if "--verbose" in args[0] or "-V" in args[0]:
        print("User prompt: ", messages)
        print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print("Response tokens: ",  response.usage_metadata.candidates_token_count)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
