import openai

# Set up your OpenAI API key
openai.api_key = 'XXX'
start_phrase = "Reiz kādā tālā zemē..."
response = openai.ChatCompletion.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "user", "content": start_phrase}
    ],
    max_tokens=100,
    temperature=0.7,
    stop=None
)

story = response.choices[0].message['content'].strip()

print(story)


