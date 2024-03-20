!pip install language_tool_python
import nltk
from nltk.tokenize import word_tokenize
from transformers import pipeline
from language_tool_python import LanguageTool

# Download NLTK resources
nltk.download('punkt')

# Initialize paraphrasing pipeline
paraphrase_pipeline = pipeline("text2text-generation", model="tuner007/pegasus_paraphrase")

def grammar_correction(text):
    """
    Perform basic grammar correction.
    """
    tool = LanguageTool('en-US')
    matches = tool.check(text)
    corrected_text = tool.correct(text)
    return corrected_text

def main():
    input_text = "He is goign to the store to buy some grocereis."

    # Grammar correction
    corrected_text_with_grammar = grammar_correction(input_text)
    print("Text with Grammar Correction:", corrected_text_with_grammar)

if __name__ == "__main__":
    main()