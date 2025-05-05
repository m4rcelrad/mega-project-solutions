import re


class PigLatin:
    """
    A class for translating words and sentences into Pig Latin.
    Pig Latin is a language game where words are altered according to specific rules.
    """
    VOWELS = "aeiouAEIOU"

    CONSONANT_BLENDS = [
        "spl", "spr", "str", "scr", "shr", "thr", "sch", "squ",
        "bl", "br", "ch", "cl", "cr", "dr", "fl", "fr",
        "gl", "gr", "pl", "pr", "sc", "sh", "sk", "sl",
        "sm", "sn", "sp", "st", "sw", "th", "tr", "tw",
        "wh", "wr"
    ]

    def __init__(self):
        pass

    def translate_word(self, word):
        """
        Translate a single word into Pig Latin according to specific rules.
        
        Rules:
        1. For words starting with vowels: add "way" to the end
        2. For words starting with consonant blends: move the blend to end and add "ay"
        3. For other consonants: move all letters before first vowel to end and add "ay"
        4. Preserve capitalization and punctuation
        
        Args:
            word: The word to be translated
            
        Returns:
            The translated word in Pig Latin
            
        Raises:
            TypeError: If input is not a string
            ValueError: If word is empty after processing punctuation
        """
        if not isinstance(word, str):
            raise TypeError(f'Expected a string, got {type(word).__name__}')
        if not word:
            return word

        punctuation = word[-1] if not word[-1].isalnum() else ""
        core = word[:-1] if punctuation else word

        if not core:
            raise ValueError("Empty word detected after stripping punctuation")

        is_capitalized = core[0].isupper()
        core = core.lower()

        if core[0] in self.VOWELS:
            pig = core + "way"
        else:
            prefix = next((b for b in sorted(self.CONSONANT_BLENDS, key=len, reverse=True) if core.startswith(b)), "")

            if prefix:
                pig = core[len(prefix):] + prefix + "ay"
            else:
                match = re.search(r"[aeiou]", core)
                if match:
                    i = match.start()
                    pig = core[i:] + core[:i] + "ay"
                else:
                    pig = core + "ay"

        if is_capitalized:
            pig = pig.capitalize()

        return pig + punctuation

    def translate_sentence(self, sentence):
        """
        Translate an entire sentence into Pig Latin while preserving:
        - Word boundaries
        - Punctuation
        - Whitespace
        
        Args:
            sentence: The sentence to be translated
            
        Returns:
            The translated sentence in Pig Latin
            
        Raises:
            TypeError: If input is not a string
        """
        if not isinstance(sentence, str):
            raise TypeError(f'Expected a string, got {type(sentence).__name__}')
        tokens = re.findall(r"\w+['’]?\w*|\W+", sentence)
        try:
            translated = [
                self.translate_word(token) if re.match(r"\w", token) else token
                for token in tokens
            ]
            return ''.join(translated)
        except ValueError as e:
            print(f"Error translating sentence: {e}")

