import os
from functions.config import *


def get_file_content(working_directory, file_path):
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