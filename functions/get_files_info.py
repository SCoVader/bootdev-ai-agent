import os
from google import genai


def get_files_info(working_directory, directory="."):
    try:
        full_path = os.path.abspath(os.path.join(os.path.abspath(working_directory), directory))

        if working_directory not in full_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(full_path):
            return f'Error: "{directory}" is not a directory'

        content = os.listdir(full_path)
        result=""
        for item in content:
            result += f" - {item}: file_size={os.path.getsize(os.path.join(full_path, item))} bytes, is_dir={os.path.isdir(os.path.join(full_path, item))}\n"

        return result
    except Exception as e:
        print(f"Error: {e}")

schema_get_files_info = genai.types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=genai.types.Schema(
        type=genai.types.Type.OBJECT,
        properties={
            "directory": genai.types.Schema(
                type=genai.types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
