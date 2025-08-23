import sys, json
import nltk
from nltk.corpus import wordnet
from transformers import pipeline
from language_tool_python import LanguageTool
import autocorrect
from autocorrect import Speller

# point nltk to local data folder
nltk.data.path.append("./nltk_data")

# initialize models
paraphrase_pipeline = pipeline("text2text-generation", model="tuner007/pegasus_paraphrase", cache_dir="./models")
tool = LanguageTool('en-US')
spell = Speller(lang='en')

def grammar_correction(text):
    matches = tool.check(text)
    return tool.correct(text)

def paraphrase(text):
    paraphrases = paraphrase_pipeline(text, max_length=50, num_return_sequences=3)
    return [p['generated_text'] for p in paraphrases]

def spell_check(text):
    return spell(text)

def combined_processing(input_text):
    spell_checked_text = spell_check(input_text)
    grammar_corrected = grammar_correction(spell_checked_text)
    paraphrases = paraphrase(grammar_corrected)

    return {
        "spell_checked": spell_checked_text,
        "grammar_corrected": grammar_corrected,
        "paraphrases": paraphrases
    }

def main():
    raw_data = sys.argv[1] if len(sys.argv) > 1 else None
    if not raw_data:
        print(json.dumps({"error": "No input provided"}))
        sys.exit(1)

    try:
        parsed = json.loads(raw_data)
        input_text = parsed.get("text", raw_data)
    except:
        input_text = raw_data

    result = combined_processing(input_text)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
