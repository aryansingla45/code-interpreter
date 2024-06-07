import subprocess

def execute_code(file_path):
    try:
        result = subprocess.run(
            ['python', file_path],
            capture_output=True,
            text=True,
            timeout=30  # Set a timeout for execution
        )
        return result.stdout if result.returncode == 0 else result.stderr
    except Exception as e:
        return str(e)
