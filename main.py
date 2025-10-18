import os
import sys
from dotenv import load_dotenv

from google import genai
from google.genai import types

from config import model_name, system_prompt, MAX_ITERS
from call_function import available_functions, call_function


def show_usage():
    print("AI Code Assistant")
    print('\nUsage: python main.py "your prompt here" [--verbose]')
    print('Example: python main.py "How do I fix the calculator?"')
    pass

def generate_content(client, messages, verbose = False):
    response = client.models.generate_content(
        model=model_name,
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], 
            system_instruction=system_prompt
        ),
    )

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if response.candidates:
        for candidate in response.candidates:
            function_call_content = candidate.content
            messages.append(function_call_content)

    if not response.function_calls:
        return response.text

    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")
        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")

    messages.append(types.Content(role="tool", parts=function_responses))


def main(*args, **kwargs):

    if len(args[0]) < 2: 
        show_usage()
        return 1

    verbose = "--verbose" in args[0] or "-V" in args[0]
    
    user_prompt = str(args[0][1])

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    
    iters = 0
    while True:
        iters += 1
        if iters >= MAX_ITERS:
            print(f"Maximum iterations ({MAX_ITERS}) reached.")
            return 1

        try:
            final_response = generate_content(client, messages, verbose)
            if final_response:
                print("Final response:")
                print(final_response)
                break
        except Exception as e:
            print(f"Error in generate_content: {e}")

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv))
