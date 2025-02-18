import openai

openai.api_key = "your-api-key-here"

def generate_code(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Write code for: {prompt}"}]
    )
    return response["choices"][0]["message"]["content"]

user_input = input("Enter a coding task: ")
print("Generated Code:\n", generate_code(user_input))
