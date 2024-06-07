import subprocess


# This function executes the code that has been generated.

def execute_code(file_path):

    # We will try to execute the code provided in the file_path.
    try:
        result = subprocess.run(
            ["python", file_path],
            capture_output=True,
            text=True,
            timeout=30,  # Set a timeout for execution
            check=True,
        )
        # If the return code is 0, it means the code executed successfully else we return the error message.
        return result.stdout if result.returncode == 0 else result.stderr
        # If an exception occurs, we return the error message.
    except Exception as e:
        return str(e)
