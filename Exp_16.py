
from collections import Counter
import string

# 1. Mock Dataset
reviews = [
    "Great product! Highly recommended.",
    "The product was okay, but delivery was late.",
    "Not worth the money. Broken on arrival."
]

# 2. Processing Pipeline
# Join all reviews into one massive string for global analysis
text_blob = " ".join(reviews).lower()

# Remove punctuation
translator = str.maketrans('', '', string.punctuation)
clean_text = text_blob.translate(translator)

# 3. Stop Word Removal (The Filter)
# Common words (stopwords) obscure the actual sentiment.
# In production, use libraries like NLTK or spaCy for this list.
stop_words = {'the', 'was', 'on', 'but', 'and', 'is', 'a', 'an'} 
tokens = [word for word in clean_text.split() if word not in stop_words]

# 4. Calculate Distribution
frequency = Counter(tokens)

print("Word Frequency (Top 5):")
print(frequency.most_common(5))