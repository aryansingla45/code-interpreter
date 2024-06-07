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

    # We are generating code based on the content of the file and the user's prompt by passing the data to OpenAI's API.
    response = generate_code(content, prompt)

    # Extract generated code and additional text from the API response
    generated_code = response.get("code", "")
    additional_text = response.get("text", "")

    # We are saving the generated code to a file.
    code_file = save_generated_code(generated_code)

    # We are executing the generated code.
    result = execute_code(code_file)

    return result



if __name__ == "__main__":
    # Example usage
    example_file_path = ""  # Add file path here
    example_user_prompt = ""  # Add prompt here

    # Process the file and get the output
    output = process_file(example_file_path, example_user_prompt)

    # Print the output
    print(output)
