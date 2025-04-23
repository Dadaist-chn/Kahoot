import openai

openai.api_key = "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"  # Replace with your actual API key

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",  # or "gpt-4" if you have access
    messages=[
        {"role": "user", "content": "Hello! Can you hear me?"}
    ]
)

print(response['choices'][0]['message']['content'])
