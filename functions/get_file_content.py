import os
from functions.config import *
from google import genai


def get_file_content(working_directory, file_path):
    try:
        full_path = os.path.abspath(os.path.join(os.path.abspath(working_directory), file_path))
    
        if working_directory not in full_path:
            return f'Error: Cannot read "{full_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'Error: File not found or is not a regular file: "{full_path}"'
    
        appendix = f'[...File "{full_path}" truncated at 10000 characters]'
    
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
        
        if os.path.getsize(full_path) > MAX_CHARS:
            file_content_string += appendix
        
        return file_content_string
    except Exception as e:
        print(f"Error: {e}")


schema_get_file_content = genai.types.FunctionDeclaration(
    name="get_file_content",
    description="Lists content of a file in the specified path, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "file_path": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The path to files, relative to the working directory. If not provided, returns an error message.",
            ),
        },
    ),
)
