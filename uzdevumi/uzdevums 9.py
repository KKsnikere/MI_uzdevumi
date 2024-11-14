import openai

# Set up your OpenAI API key
openai.api_key = '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'
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


