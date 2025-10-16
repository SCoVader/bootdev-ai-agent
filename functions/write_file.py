import os
from google import genai


def write_file(working_directory, file_path, content):
    try:
        full_path = os.path.abspath(os.path.join(os.path.abspath(working_directory), file_path))
    
        if working_directory not in full_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        # if not os.path.exists(full_path):
        with open(full_path, "w") as f:
            f.write(content)

    except Exception as e:
        print(f"Error: {e}")

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


schema_write_file = genai.types.FunctionDeclaration(
    name="write_file",
    description="Creates file in specified path, if a file already exists then rewrites it, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "directory": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The path where file will be created or rewriten, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
            "content": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="Content that will be placed in specified file. Created or existing",
            ),
        },
    ),
)
