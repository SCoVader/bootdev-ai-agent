import os
import subprocess
import sys

def run_python_file(working_directory, file_path, args=[]):
    try:
        full_path = os.path.abspath(os.path.join(os.path.abspath(working_directory), file_path))
    
        if working_directory not in full_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(full_path):
            return f'Error: File "{file_path}" not found.'
        if not str(full_path).endswith(".py"):
            return f'Error: "{file_path}" is not a Python file.'
    except Exception as e:
        print(f"Error:{e}")
        
    args_combined=["python", full_path ]
    args_combined.extend(args)

    try:
        # print(f"DEBUG: {args_combined}")
        # print(f"DEBUG: {os.path.abspath(working_directory)}")
    
        compleated_proc = subprocess.run(args=args_combined, timeout=30, capture_output=True, cwd=os.path.abspath(working_directory), text=True)

        proc_results="" 
        if not compleated_proc.stdout:
            proc_results += "No output produced.\n"
        else:
            proc_results += str(f"STDOUT:{compleated_proc.stdout}\n")
        if compleated_proc.stderr:
            proc_results += str(f"STDERR:{compleated_proc.stderr}\n")
        if compleated_proc.returncode != 0:
            proc_results += f"Process exited with code {compleated_proc.returncode}\n"
        return proc_results
    except Exception as e:
        print(f"Error: executing Python file: {e}")
        

