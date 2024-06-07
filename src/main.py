from file_reader import read_pdf, read_xlsx, read_csv, read_docx
from code_generator import generate_code, save_generated_code
from code_executor import execute_code


def process_file(file_path, prompt):
    if file_path.endswith(".pdf"):
        content = read_pdf(file_path)
    elif file_path.endswith(".xlsx"):
        content = read_xlsx(file_path)
    elif file_path.endswith(".csv"):
        content = read_csv(file_path)
    elif file_path.endswith(".docx"):
        content = read_docx(file_path)
    else:
        return "Unsupported file type"

    code = generate_code(content, prompt)
    code_file_path = save_generated_code(code)
    result = execute_code(code_file_path)

    return result


if __name__ == "__main__":
    # Example usage
    example_file_path = ""  # Add file path here
    example_user_prompt = ""  # Add prompt here

    # Process the file and get the output
    output = process_file(example_file_path, example_user_prompt)

    # Print the output
    print(output)
