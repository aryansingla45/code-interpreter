import openai

def generate_code(prompt):
    openai.api_key = 'your-api-key'
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.5,
    )
    return response.choices[0].text.strip()

# Example usage
# prompt = "Given the following CSV content, generate a Python function to calculate the average of a column."
# code = generate_code(prompt + "\n" + csv_content)
# print(code)
