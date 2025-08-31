from openai import OpenAI

# create client (replace with your actual key)
client = OpenAI(api_key="<YOUR_KEY_HERE>")

completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant named Jarvis."},
        {"role": "user", "content": "what is coding"}
    ]
)

print(completion.choices[0].message.content)
