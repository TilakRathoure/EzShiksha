import re
import sys
import json
from spellchecker import SpellChecker

# Common grammar patterns to fix
GRAMMAR_PATTERNS = [
    # Basic contractions (highest priority)
    (r'\bdoes\s+not\b', "doesn't"),
    (r'\bdo\s+not\b', "don't"),
    (r'\bis\s+not\b', "isn't"),
    (r'\bare\s+not\b', "aren't"),
    (r'\bam\s+not\b', "ain't"),
    
    # Subject-verb agreement with doesn't/don't
    (r'\b(he|she|it)\s+dont\b', r"\1 doesn't"),
    (r'\b(he|she|it)\s+don\'t\b', r"\1 doesn't"),
    (r'\b(i|you|we|they)\s+doesnt\b', r"\1 don't"),
    (r'\b(i|you|we|they)\s+doesn\'t\b', r"\1 don't"),
    (r'\b(he|she|it)\s+have\b', r"\1 has"),
    (r'\b(he|she|it)\s+got\b', r"\1 has"),
    
    # Double negatives and incorrect forms (must come after subject-verb agreement)
    (r'\b(he|she|it)\s+doesn\'t\s+have\s+no\b', r"\1 doesn't have any"),
    (r'\b(i|you|we|they)\s+don\'t\s+have\s+no\b', r"\1 don't have any"),
    (r'\b(he|she|it)\s+doesn\'t\s+got\b', r"\1 doesn't have"),
    (r'\b(i|you|we|they)\s+don\'t\s+got\b', r"\1 don't have"),
    
    # Basic pronouns and contractions
    (r'\bdoes\s+not\b', "doesn't"),
    (r'\bdo\s+not\b', "don't"),
    (r'\bis\s+not\b', "isn't"),
    (r'\bare\s+not\b', "aren't"),
    (r'\bam\s+not\b', "ain't"),
    (r'\bdont\b', "don't"),
    (r'\bdoesnt\b', "doesn't"),
    (r'\bwont\b', "won't"),
    (r'\bcant\b', "can't"),
    (r'\bhasnt\b', "hasn't"),
    (r'\bhavent\b', "haven't"),
    (r'\baint\b', "isn't"),
    (r'\bwasnt\b', "wasn't"),
    (r'\bwerent\b', "weren't"),
    (r'\bwouldnt\b', "wouldn't"),
    (r'\bcouldnt\b', "couldn't"),
    (r'\bshouldnt\b', "shouldn't"),
    
    # Subject-verb agreement
    (r'\bi\s+(is|are)\b', 'I am'),
    (r'\byou\s+is\b', 'you are'),
    (r'\bhe\s+are\b', 'he is'),
    (r'\bshe\s+are\b', 'she is'),
    (r'\bit\s+are\b', 'it is'),
    (r'\bthey\s+is\b', 'they are'),
    (r'\bwe\s+is\b', 'we are'),
    (r'\b(i|you|we|they)\s+has\b', r'\1 have'),
    
    # Verb forms
    (r'\bis\s+want\b', 'wants'),
    (r'\bare\s+want\b', 'want'),
    (r'\bam\s+want\b', 'want'),
    (r'\b(is|are|am)\s+going\s+to\b', 'will'),
    (r'\b(is|are)\s+wanting\b', 'want'),
    (r'\bfor (buy|go|drink|eat|sleep|run|walk)\b', r'to \1'),
    (r'\bto\s+drinking\b', 'to drink'),
    (r'\bto\s+eating\b', 'to eat'),
    (r'\bto\s+sleeping\b', 'to sleep'),
    (r'\bto\s+running\b', 'to run'),
    (r'\bto\s+walking\b', 'to walk'),
    (r'\bfor\s+(buy|go|drink|eat|sleep|run|walk)ing\b', r'to \1'),
    
    # Present continuous fixes
    (r'\b(am|is|are)\s+(.*?)ing\b', r'\1 \2ing'),
    (r'\b(was|were)\s+(.*?)ing\b', r'\1 \2ing'),
    
    # Future tense
    (r'\bgoing\s+to\s+(.*?)\b', r'will \1'),
    (r'\bam\s+going\s+to\s+(.*?)\b', r'will \1'),
    (r'\bis\s+going\s+to\s+(.*?)\b', r'will \1'),
    (r'\bare\s+going\s+to\s+(.*?)\b', r'will \1'),
    
    # Articles
    (r'\ban\s+([^aeiouAEIOU\s])', r'a \1'),
    (r'\ba\s+([aeiouAEIOU])', r'an \1'),
    
    # Prepositions
    (r'\bin\s+(the\s+)?(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b', r'on \1\2'),
    (r'\bin\s+(the\s+)?(january|february|march|april|may|june|july|august|september|october|november|december)\b', r'in \1\2'),
    (r'\bin\s+([0-9]+)\s+(am|pm)\b', r'at \1 \2'),
    
    # Subject-specific negatives (must come before other negative patterns)
    (r'\b(he|she|it)\s+dont\s+have\s+no\b', r"\1 doesn't have any"),
    (r'\b(he|she|it)\s+don\'t\s+have\s+no\b', r"\1 doesn't have any"),
    (r'\b(i|you|we|they)\s+doesnt\s+have\s+no\b', r"\1 don't have any"),
    (r'\b(i|you|we|they)\s+doesn\'t\s+have\s+no\b', r"\1 don't have any"),
    
    # General double negatives
    (r'\bdont\s+have\s+no\b', "don't have any"),
    (r'\bdoesnt\s+have\s+no\b', "doesn't have any"),
    (r'\bdoesn\'t\s+have\s+no\b', "doesn't have any"),
    (r'\bdon\'t\s+have\s+no\b', "don't have any"),
    (r'\baint\s+got\s+no\b', "don't have any"),
    (r'\bwont\s+have\s+no\b', "won't have any"),
    (r'\bwon\'t\s+have\s+no\b', "won't have any"),
    
    # Common phrases
    (r'\bin\s+order\s+to\s+to\b', 'in order to'),
    (r'\bmore\s+better\b', 'better'),
    (r'\bmost\s+best\b', 'best'),
    (r'\bvery\s+much\s+(big|small|tall|short)\b', r'very \1'),
    
    # Plural fixes
    (r'\b(\d+)\s+person\b', r'\1 people'),
    (r'\bone\s+persons\b', 'one person'),
    
    # Redundancy
    (r'\breturn\s+back\b', 'return'),
    (r'\brepeat\s+again\b', 'repeat'),
    (r'\bfirst\s+began\b', 'began'),
    
    # Progressive tense
    (r'\b(is|are|was|were)\s+been\b', r'\1'),
    (r'\bhave\s+been\s+being\b', 'have been'),
    
    # Wrong word forms
    (r'\bmore\s+easier\b', 'easier'),
    (r'\bmost\s+easiest\b', 'easiest'),
    (r'\bmore\s+harder\b', 'harder'),
    (r'\bmost\s+hardest\b', 'hardest'),
    
    # Time expressions
    (r'\bin\s+night\b', 'at night'),
    (r'\bin\s+morning\b', 'in the morning'),
    (r'\bin\s+evening\b', 'in the evening'),
    
    # Common errors with infinitives
    (r'\b(want|needs|likes|tries)\s+eating\b', r'\1 to eat'),
    (r'\b(want|needs|likes|tries)\s+doing\b', r'\1 to do'),
    (r'\b(want|needs|likes|tries)\s+going\b', r'\1 to go'),
    
    # Capitalization after punctuation
    (r'(\.|!|\?)\s*([a-z])', lambda m: m.group(1) + ' ' + m.group(2).upper()),
    
    # Case-sensitive replacements (must be last)
    (r'(^|[.!?]\s+)([a-z])', lambda m: m.group(1) + m.group(2).upper()),
    (r'\b(monday|tuesday|wednesday|thursday|friday|saturday|sunday)\b', lambda m: m.group(1).capitalize()),
    (r'\b(january|february|march|april|may|june|july|august|september|october|november|december)\b', lambda m: m.group(1).capitalize())
]

class GrammarCorrector:
    def __init__(self):
        """
        Initialize the lightweight spell checker.
        """
        self.spellchecker = SpellChecker()

    def _apply_grammar_rules(self, text: str) -> str:
        """
        Apply basic grammar correction rules.
        """
        text = ' ' + text + ' '  # Add spaces to help with word boundary matching
        for pattern, replacement in GRAMMAR_PATTERNS:
            text = re.sub(pattern, replacement, text, flags=re.IGNORECASE)
        return text.strip()

    def correct(self, text: str) -> str:
        """
        Perform grammar and spell correction on the input text.
        """
        # Clean and limit input
        text = text.strip().replace("\n", " ")
        text = re.sub(r'\s+', ' ', text)  # Normalize whitespace
        if len(text.split()) > 200:  # Limit input size
            text = ' '.join(text.split()[:200])

        # Split into words while preserving spacing
        words = []
        current = []
        
        # Apply grammar rules first
        text = self._apply_grammar_rules(text)
        
        # Process each word individually
        word_pattern = re.compile(r'(\b\w+\b|\s+|[^\w\s])')
        matches = word_pattern.finditer(text)
        
        result = []
        for match in matches:
            token = match.group(0)
            if token.strip() and any(c.isalpha() for c in token):
                # It's a word - spell check it
                corrected = self.spellchecker.correction(token.lower())
                if not corrected:
                    corrected = token
                    
                # Preserve original capitalization
                if token.istitle():
                    corrected = corrected.capitalize()
                elif token.isupper():
                    corrected = corrected.upper()
                    
                result.append(corrected)
            else:
                # Keep punctuation and whitespace as is
                result.append(token)
        
        # Join into text
        text = ''.join(result)
        
        # Process sentence capitalization
        sentences = []
        for sentence in re.split(r'([.!?]+)', text):
            if sentence.strip():
                if not any(c in '.!?' for c in sentence):
                    # It's the sentence content
                    sentence = sentence.strip()
                    if sentence:
                        sentence = sentence[0].upper() + sentence[1:] if len(sentence) > 1 else sentence.upper()
                sentences.append(sentence)
                
        text = ''.join(sentences)
            
        return text.strip()


if __name__ == "__main__":
    try:
        # Get input text from command line arg
        input_text = sys.argv[1] if len(sys.argv) > 1 else "i is want watar to drinking. she dont care. they is going to store."
        
        # Initialize corrector and process text
        corrector = GrammarCorrector()
        result = corrector.correct(input_text)
        print(f"Correct: {result}")
        sys.exit(0)
    except Exception as e:
        print(f"Error: {str(e)}", file=sys.stderr)
        sys.exit(1)
