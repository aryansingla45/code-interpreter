import os
import openai

# Set your OpenAI API key here
openai.api_key = "your-openai-api-key"


def generate_code(file_content, user_prompt):
    # Define the prompt for the OpenAI API
    prompt = f"The user has provided the following file content:\n{file_content}\n\nUser's request: {user_prompt}\n\nGenerate Python code to fulfill the user's request."

    # Call the OpenAI API to generate code based on the prompt
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # Extract the generated code from the API response
    code = response.choices[0].text.strip()
    return code

# Save the generated code to a file so that we can execute it later
def save_generated_code(code, folder="artifacts", filename="generated_code.py"):
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, filename)
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(code)
    return file_path
