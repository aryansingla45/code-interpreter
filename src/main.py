from file_reader import read_pdf, read_xlsx, read_csv, read_docx
from code_generator import generate_code, save_generated_code
from code_executor import execute_code

def process_file(file_path, file_type, user_prompt):
    if file_type == 'pdf':
        content = read_pdf(file_path)
    elif file_type == 'xlsx':
        content = read_xlsx(file_path)
    elif file_type == 'csv':
        content = read_csv(file_path)
    elif file_type == 'docx':
        content = read_docx(file_path)
    else:
        return "Unsupported file type"
    
    code = generate_code(content, user_prompt)
    code_file_path = save_generated_code(code)
    result = execute_code(code_file_path)
    
    return result

if __name__ == "__main__":
    file_path = 'path_to_file.pdf'
    file_type = 'pdf'  # 'pdf', 'xlsx', 'csv', or 'docx'
    user_prompt = 'Summarize the data'
    output = process_file(file_path, file_type, user_prompt)
    print(output)
