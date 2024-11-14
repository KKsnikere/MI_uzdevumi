import re
raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"
# Clean text: remove mentions, URLs, duplicate punctuation, emojis, and convert to lowercase
cleaned_text = re.sub(r'@\w+|http\S+|([!?])\1+|[^\w\s]', r'\1', raw_text).strip().lower()

print(cleaned_text)
