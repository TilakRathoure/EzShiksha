pip install autocorrect
from autocorrect import Speller

def spell_check(text):
    """
    Correct spelling mistakes in the input text.
    """
    spell = Speller(lang='en')
    corrected_text = spell(text)
    return corrected_text

def main():
    input_text = "He is goign to the store to buy some grocereis."

    # Spell check
    corrected_text = spell_check(input_text)
    print("Spell-checked Text:", corrected_text)

if __name__ == "__main__":
    main()