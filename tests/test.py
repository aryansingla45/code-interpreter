from src.main import process_file

if __main__ == "__main__":
    # Example usage
    example_file_path = "tests/test.pdf"
    example_user_prompt = "Generate a Python script to read the content of this PDF file."

    # Process the file and get the output
    output = process_file(example_file_path, example_user_prompt)

    # Print the output
    print(output)