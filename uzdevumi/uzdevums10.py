import openai
openai.api_key = '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'
texts_lv = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

translations = []
for text in texts_lv:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": f"Translate the following text to English: {text}"}
        ],
        max_tokens=100,
        temperature=0.7,
        stop=None
    )
    translation = response.choices[0].message['content'].strip()
    translations.append(translation)
for original, translated in zip(texts_lv, translations):
    print(f"Original: {original}\nTranslated: {translated}\n")
