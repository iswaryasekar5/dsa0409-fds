import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt

def analyze_feedback(file_path):
    # 1. Load Dataset
    try:
        df = pd.read_csv(file_path)
        # Ensure column exists
        if 'feedback' not in df.columns:
            print("Error: CSV must contain a 'feedback' column.")
            return
    except FileNotFoundError:
        print("Error: File not found.")
        return

    # 2. Define Stop Words
    # In production, use: from nltk.corpus import stopwords; stop_words = set(stopwords.words('english'))
    stop_words = {
        "the", "and", "is", "to", "in", "of", "it", "that", "this", "for",
        "was", "but", "not", "my", "on", "with", "as", "at", "by", "an", "be", "i"
    }

    # 3. Preprocessing & Tokenization
    all_words = []
    
    # Efficient string translation table for punctuation removal
    translator = str.maketrans('', '', string.punctuation)

    for text in df['feedback'].dropna():
        # Lowercase and strip punctuation
        clean_text = str(text).lower().translate(translator)
        # Filter stop words and split
        words = [w for w in clean_text.split() if w not in stop_words]
        all_words.extend(words)

    # 4. Calculate Frequency
    word_counts = Counter(all_words)

    # 5. User Input for N
    try:
        N = int(input("Enter the number of top frequent words to display (N): "))
    except ValueError:
        print("Invalid input. Defaulting to 5.")
        N = 5

    top_words = word_counts.most_common(N)
    
    # Display Text Results
    print(f"\n--- Top {N} Most Frequent Words ---")
    for word, count in top_words:
        print(f"{word}: {count}")

    # 6. Plotting
    if top_words:
        words, counts = zip(*top_words)
        plt.figure(figsize=(10, 6))
        plt.bar(words, counts, color='skyblue')
        plt.xlabel('Words')
        plt.ylabel('Frequency')
        plt.title(f'Top {N} Most Frequent Words in Feedback')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        print("No words found to plot.")

# Execution (assuming data.csv exists)
if __name__ == "__main__":
    # Create a small sample CSV and run analysis for quick testing
    sample = pd.DataFrame({
        "feedback": [
            "The course was excellent and very helpful.",
            "I liked the instructor but the pace was fast.",
            "Good content, but I want more examples.",
            "The labs were useful and the instructor was clear.",
            "Great course overall; I learned a lot."
        ]
    })
    sample_path = r"c:\Users\MOHAN KUMAR\OneDrive\Desktop\FDS\sample_feedback.csv"
    sample.to_csv(sample_path, index=False)
    analyze_feedback(sample_path)