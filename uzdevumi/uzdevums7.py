from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('distiluse-base-multilingual-cased')
words = ["māja", "dzīvoklis", "jūra"]
word_embeddings = model.encode(words)

similarities = {}
for i in range(len(words)):
    for j in range(i + 1, len(words)):
        similarity = util.cos_sim(word_embeddings[i], word_embeddings[j]).item()
        similarities[(words[i], words[j])] = similarity

print("Semantic similarity between words:")
for (word1, word2), similarity in similarities.items():
    print(f"{word1} - {word2}: similarity = {similarity:.2f}")
