from collections import Counter
import re

#text = input("Ievadiet tekstu: ")
text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."
normalized_text = re.sub(r'[^a-zA-Zāčēģīķņšūžż ]', '', text.lower())
words = normalized_text.split()
word_frequencies = Counter(words)
for word, frequency in word_frequencies.items():
    print(f"{word}: {frequency}")