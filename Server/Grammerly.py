import sys
import json
import os
from language_tool_python import LanguageTool

tool = LanguageTool('en-US', cache_dir=os.getenv("LT_CACHE_DIR"))


# ------------------ Functions ------------------ #
def grammar_and_spell_correction(text):
    """
    Corrects both grammar and spelling using LanguageTool.
    """
    corrected_text = tool.correct(text)
    return corrected_text

# ------------------ Main ------------------ #
def main():
    raw_data = sys.argv[1] if len(sys.argv) > 1 else None
    if not raw_data:
        print(json.dumps({"error": "No input provided"}))
        sys.exit(1)

    try:
        parsed = json.loads(raw_data)
        input_text = parsed.get("text", raw_data)
    except json.JSONDecodeError:
        input_text = raw_data

    corrected_text = grammar_and_spell_correction(input_text)
    print(corrected_text)

if __name__ == "__main__":
    main()
