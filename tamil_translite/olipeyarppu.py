import json
import pkg_resources
# list of vallinam,mellinam,idaiyinam
vallinam = ["க", "ச", "ட", "த", "ப", "ற"]
mellinam = ["ங", "ஞ", "ண", "ந", "ம", "ன"]
idaiyinam = ["ய", "ர", "ல", "வ", "ழ", "ள"]

# Phonetic pronouncation
json_file_path = pkg_resources.resource_filename(__name__, "translit_rules.json")
with open(json_file_path, "r", encoding="utf-8") as file:
    transliteration_rules = json.load(file)

ka_rule = transliteration_rules.get("ka_rule", {})
sa_rule = transliteration_rules.get("sa_rule", {})
ta_rule = transliteration_rules.get("ta_rule", {})
pa_rule = transliteration_rules.get("pa_rule", {})
tha_rule = transliteration_rules.get("tha_rule", {})
extras = transliteration_rules.get("extras", {})


# Combines constanant with vowel sign
def extras_comb(letter):
    return [letter + const for const in extras]


# Rules
def olipeyarppu(word_start, tam_word, prev_comb, next_next_char, next_char):
    roman_text = ""
    if word_start:
        if tam_word in extras_comb("க"):
            roman_text += ka_rule.get(tam_word, {})

        elif tam_word in extras_comb("த"):
            roman_text += tha_rule.get(tam_word, {})

        elif tam_word in extras_comb("ட")[2:]:
            roman_text += ta_rule.get(tam_word, {})

        elif tam_word in extras_comb("ப"):
            roman_text += pa_rule.get(tam_word, {})

        else:
            roman_text += transliteration_rules["letter_rule"].get(tam_word, {})

    elif tam_word == "க" and prev_comb == "று":
        roman_text += "ka"

    elif (
        prev_comb
        in [letter + "்" for letter in vallinam + idaiyinam + mellinam + ["ஸ", "ஷ"]]
        and prev_comb != "ங்"
    ):

        if prev_comb == "ன்":
            if tam_word == "று":
                roman_text += "dru"
            elif tam_word == "றி":
                roman_text += "dri"
            elif tam_word == "ற":
                roman_text += "dra"
            elif tam_word == "றை":
                roman_text += "drai"
            elif tam_word in extras_comb("ப"):
                roman_text += transliteration_rules["letter_rule"].get(tam_word, "")

        if roman_text == "" and prev_comb in ["க்", "ச்", "ட்", "த்", "ப்", "ற்", "ஷ்", "ஸ்"]:

            roman_text += ka_rule.get(tam_word, "")
            roman_text += sa_rule.get(tam_word, "")
            roman_text += ta_rule.get(tam_word, "")
            roman_text += tha_rule.get(tam_word, "")
            roman_text += pa_rule.get(tam_word, "")
        if roman_text == "":
            roman_text += transliteration_rules["letter_rule"].get(tam_word, "")

    elif prev_comb in ["ஞ்", "ங்"]:
        for key, value in extras.items():
            if tam_word in [letter + key for letter in vallinam]:
                roman_text += value

    elif tam_word == "ற்" and next_next_char == "ற":
        roman_text += "t"

    else:
        roman_text += transliteration_rules["letter_rule"].get(tam_word, "")

    return roman_text
