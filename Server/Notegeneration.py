import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from heapq import nlargest
import sys
import json
nltk.data.path.append("./nltk_data")

data = sys.argv[1] if len(sys.argv) > 1 else None

if not data:
    print("Error: No input essay provided.")
    sys.exit(1)

sample_essay = data

def generate_summary(essay):
    try:
        # Tokenize the essay into sentences
        sentences = sent_tokenize(essay)

        # Preprocess the sentences
        stop_words = set(stopwords.words('english'))
        word_frequencies = {}
        for sentence in sentences:
            words = nltk.word_tokenize(sentence.lower())
            for word in words:
                if word not in stop_words:
                    if word not in word_frequencies:
                        word_frequencies[word] = 1
                    else:
                        word_frequencies[word] += 1

        # Calculate weighted frequencies for each sentence
        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word] / max_frequency)

        # Calculate scores for each sentence
        sentence_scores = {}
        for sentence in sentences:
            for word in nltk.word_tokenize(sentence.lower()):
                if word in word_frequencies.keys():
                    if len(sentence.split(' ')) < 30:
                        if sentence not in sentence_scores.keys():
                            sentence_scores[sentence] = word_frequencies[word]
                        else:
                            sentence_scores[sentence] += word_frequencies[word]

        # Get top 3 sentences based on scores for summary
        summary_sentences = nlargest(3, sentence_scores, key=sentence_scores.get)
        summary = ' '.join(summary_sentences)
        return summary
    except Exception as e:
        print(f"Error in generate_summary: {e}")
        return "Error generating summary."

def generate_notes(essay, num_notes=10):
    try:
        # Tokenize the essay into sentences
        sentences = sent_tokenize(essay)

        # Preprocess the sentences
        stop_words = set(stopwords.words('english'))
        word_frequencies = {}
        for sentence in sentences:
            words = nltk.word_tokenize(sentence.lower())
            for word in words:
                if word not in stop_words:
                    if word not in word_frequencies:
                        word_frequencies[word] = 1
                    else:
                        word_frequencies[word] += 1

        # Calculate weighted frequencies for each sentence
        max_frequency = max(word_frequencies.values())
        for word in word_frequencies.keys():
            word_frequencies[word] = (word_frequencies[word] / max_frequency)

        # Calculate scores for each sentence
        sentence_scores = {}
        for sentence in sentences:
            for word in nltk.word_tokenize(sentence.lower()):
                if word in word_frequencies.keys():
                    if len(sentence.split(' ')) < 30:
                        if sentence not in sentence_scores.keys():
                            sentence_scores[sentence] = word_frequencies[word]
                        else:
                            sentence_scores[sentence] += word_frequencies[word]

        # Get top N sentences based on scores for notes
        summary_sentences = nlargest(num_notes, sentence_scores, key=sentence_scores.get)
        return summary_sentences
    except Exception as e:
        print(f"Error in generate_notes: {e}")
        return ["Error generating notes."]

def main():
    try:
        # Use the sample input essay
        essay = sample_essay

        if not essay:
            print("Error: The essay is empty or invalid.")
            sys.exit(1)

        # Generate summary
        summary = generate_summary(essay)
        print("Summary of the essay:")
        print(summary)
        print("\n")

        # Generate notes
        notes = generate_notes(essay)
        print("Generated notes:")
        for i, note in enumerate(notes):
            print(f"{i+1}: {note}")
    except Exception as e:
        print(f"Error in main function: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
