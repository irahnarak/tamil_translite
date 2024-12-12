import json
import re
import pkg_resources

from .olipeyarppu import olipeyarppu

json_file_path = pkg_resources.resource_filename(__name__, "translit_rules.json")

# Open the file with the absolute path
with open(json_file_path, "r", encoding="utf-8") as file:
    transliteration_rules = json.load(file)

# Some special cases
special_case = transliteration_rules.get("special_case", {})


# Replace the tam_word with special case word
def replace_word(match):
    word = match.group(0)
    return special_case.get(word, "")


# Main function for transliteration
def translite(tamil_text):

    roman_text = ""
    word_start = True
    i = 0

    # Identifying patter for special case
    pattern = r"|".join(re.escape(key) for key in special_case.keys())
    tamil_text = re.sub(pattern, replace_word, tamil_text)
    while i < len(tamil_text):
        if (
            i + 1 < len(tamil_text)
            and tamil_text[i : i + 2] in transliteration_rules["letter_rule"]
        ):
            ########### const+vowels (like - கி, மீ) ###########

            tam_word = tamil_text[i : i + 2] if i + 1 < len(tamil_text) else ""
            prev_comb = tamil_text[i - 2 : i] if i - 2 >= 0 else ""
            next_next_char = tamil_text[i + 2] if i + 2 < len(tamil_text) else ""
            next_char = tamil_text[i + 1] if i + 1 < len(tamil_text) else ""

            roman_text += olipeyarppu(
                word_start, tam_word, prev_comb, next_next_char, next_char
            )

            i += 1  # Skip the next character as it's already processed

            word_start = False  # After processing the first character, it's no longer at the letter_rule

        ########### Handle single characters like அ, த ###########

        elif tamil_text[i] in transliteration_rules["letter_rule"]:
            tam_word = tamil_text[i]
            next_char = tamil_text[i + 1] if i + 1 < len(tamil_text) else ""
            prev_comb = tamil_text[i - 2 : i] if i - 2 >= 0 else ""
            next_next_char = tamil_text[i + 2] if i + 2 < len(tamil_text) else ""
            roman_text += olipeyarppu(
                word_start, tam_word, prev_comb, next_next_char, next_char
            )

        else:
            roman_text += tamil_text[
                i
            ]  # If no mapping exists, keep the character as it is

        i += 1
        word_start = False

        # Handle word boundary detection by checking if the next character is a space
        if i < len(tamil_text) and tamil_text[i - 1] in [
            " ",
            "\n",
            ",",
            ";",
            ":",
            "'",
            "-",
            "_",
            "(",
            ")",
            ".",
            "$",
            "@",
            "#",
            "%",
            "*",
        ]:
            word_start = True  # Reset word letter_rule for next word

    return roman_text.strip()
