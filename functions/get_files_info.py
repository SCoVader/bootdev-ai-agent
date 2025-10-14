import os

# - README.md: file_size=1032 bytes, is_dir=False
# - src: file_size=128 bytes, is_dir=True
# - package.json: file_size=1234 bytes, is_dir=False

def get_files_info(working_directory, directory="."):

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
