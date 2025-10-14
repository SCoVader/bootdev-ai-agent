import os


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