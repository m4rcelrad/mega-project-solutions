import re


class PigLatin:
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

    def translate_word(self, word: str) -> str:
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

    def translate_sentence(self, sentence: str) -> str:
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

