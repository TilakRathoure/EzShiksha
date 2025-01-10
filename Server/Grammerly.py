import sys
import json  # Import the json module

# Parse the JSON string received from sys.argv[1]

# Access the "channel" property from the parsed JSON object


import nltk
from nltk.tokenize import word_tokenize
from transformers import pipeline
from language_tool_python import LanguageTool
from nltk.corpus import wordnet
from autocorrect import Speller

# Download NLTK resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
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

def grammar_correction(text):
    """
    Perform basic grammar correction.
    """
    tool = LanguageTool('en-US')
    matches = tool.check(text)
    corrected_text = tool.correct(text)
    return corrected_text

def paraphrase(text):
    """
    Generate paraphrases for the input text.
    """
    paraphrases = paraphrase_pipeline(text, max_length=50, num_return_sequences=3)
    return [paraphrase['generated_text'] for paraphrase in paraphrases]

def spell_check(text):
    """
    Correct spelling mistakes in the input text.
    """
    spell = Speller(lang='en')
    corrected_text = spell(text)
    return corrected_text

def combined_processing(input_text):
    """
    Perform spell check, grammar correction, and paraphrasing.
    """
    # Spell check
    spell_checked_text = spell_check(input_text)
    print("Spell-checked Text:", spell_checked_text)
    print()

    # Grammar correction
    corrected_text_with_grammar = grammar_correction(spell_checked_text)
    print("Text with Grammar Correction:", corrected_text_with_grammar)

    # Paraphrasing
    paraphrases = paraphrase(corrected_text_with_grammar)
    print("Paraphrases:")
    for idx, para in enumerate(paraphrases):
        print(f"{idx + 1}. {para}")

    return spell_checked_text, corrected_text_with_grammar, paraphrases

data = sys.argv[1]

def main():
    # input_text = "He is goign to the store to buy some grocereis."
    combined_processing(data)
    


if __name__ == "__main__":
    main()