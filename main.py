import os
import sys
from dotenv import load_dotenv
from google import genai


def show_usage():
    print("Boot.dev ai agent")
    print("\nUsage: main \"your question or request\" [--verbose]")
    pass

def main(*args, **kwargs):
    request = ""

    if len(args[0]) < 2: 
        show_usage()
        return 1

    # print(args[0][1])
    
    request = str(args[0][1])


    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=request
    )

    print(response.text)
    
    if "--verbose" in args[0] or "-V" in args[0]:
        print("User prompt: ", request)
        print("Prompt tokens: ", response.usage_metadata.prompt_token_count)
        print("Response tokens: ",  response.usage_metadata.candidates_token_count)

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
