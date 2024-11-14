import spacy
from spacy.lang.lv import Latvian

nlp = Latvian()
nlp.add_pipe('sentencizer')

article = (
    "Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru "
    "un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļūve Baltijas jūrai. "
    "Tā ir viena no Eiropas Savienības dalībvalstīm."
)
doc = nlp(article)

# Extracting key sentences
sentences = list(doc.sents)
summary = f"{sentences[0].text} {sentences[2].text}"

print(summary)
