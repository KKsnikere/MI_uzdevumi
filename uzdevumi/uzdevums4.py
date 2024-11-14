from transformers import pipeline
sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]
classifier = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

for sentence in sentences:
    result = classifier(sentence)[0]
    label = result['label']
    if '1' in label:
        sentiment = 'negatīvs'
    elif '5' in label:
        sentiment = 'pozitīvs'
    else:
        sentiment = 'neitrāls'
    print(f"Teikums: '{sentence}' - Noskaņojums: {sentiment}")