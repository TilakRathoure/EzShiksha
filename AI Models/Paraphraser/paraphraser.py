import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet
nltk.download('averaged_perceptron_tagger')
from transformers import pipeline

# Download NLTK resources
nltk.download('punkt')
nltk.download('wordnet')


# Initialize paraphrasing pipeline
paraphrase_pipeline = pipeline("text2text-generation", model="tuner007/pegasus_paraphrase")

def get_wordnet_pos(treebank_tag):
    """
    Map Treebank POS tags to WordNet POS tags.
    """
    if treebank_tag.startswith('J'):
        return wordnet.ADJ
    elif treebank_tag.startswith('V'):
        return wordnet.VERB
    elif treebank_tag.startswith('N'):
        return wordnet.NOUN
    elif treebank_tag.startswith('R'):
        return wordnet.ADV
    else:
        return None



def paraphrase(text):
    """
    Generate paraphrases for the input text.
    """
    paraphrases = paraphrase_pipeline(text, max_length=50, num_return_sequences=3)
    return [paraphrase['generated_text'] for paraphrase in paraphrases]

def grammar_correction(text):
    """
    Perform basic grammar correction.
    """
    tokens = word_tokenize(text)
    # Part-of-speech tagging
    pos_tags = nltk.pos_tag(tokens)
    # Check and correct verb forms
    for i, (token, pos_tag) in enumerate(pos_tags):
        if pos_tag.startswith('VB'):
            # Check if the word exists in WordNet
            synsets = wordnet.synsets(token)
            if not synsets:
                continue
            # Get WordNet POS tag
            wn_pos = get_wordnet_pos(pos_tag)
            if not wn_pos:
                continue
            # Get all lemmas for the word and filter by POS
            lemmas = set()
            for synset in synsets:
                lemmas.update([lemma.name() for lemma in synset.lemmas() if lemma.synset().pos() == wn_pos])
            if not lemmas:
                continue
            # Replace the verb with the first lemma found
            tokens[i] = lemmas.pop()
    return ' '.join(tokens)

def main():
    input_text = "He is goign to the store to buy some grocereis."


    # Paraphrasing
    paraphrases = paraphrase(input_text)
    print("Paraphrases:")
    for idx, para in enumerate(paraphrases):
        print(f"{idx + 1}. {para}")

    # Grammar correction
    corrected_text_with_grammar = grammar_correction(input_text)
    print("Text with Grammar Correction:", corrected_text_with_grammar)

main()