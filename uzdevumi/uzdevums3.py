from sentence_transformers import SentenceTransformer, util

text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."
model = SentenceTransformer('distiluse-base-multilingual-cased')
embedding1 = model.encode(text1, convert_to_tensor=True)
embedding2 = model.encode(text2, convert_to_tensor=True)
cosine_similarity = util.pytorch_cos_sim(embedding1, embedding2).item() * 100

print(f"Tekstu sakritības līmenis: {cosine_similarity:.2f}%")
