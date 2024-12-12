
# Tamil_Translite

**Tamil_Translite** is a Python library designed to transliterate Tamil words to English.

## Features

- **Phonetic Transliteration**: Offers transliteration of Tamil words into the Roman alphabet, maintaining their phonetic integrity.

  ### Examples:
  - கல் → kal
  - பொங்கல் → pongal
  - வருத்தம் → varuththam
  - மருதம் → marudham


- **Helpful for Tamil Learners**: Assists individuals learning Tamil by offering an easy-to-use transliteration tool, aiding in pronunciation and comprehension of Tamil words.

## Installation

You can install `tamil_translite` from PyPI using `pip`:

```bash
pip install tamil_translite
```

## Usage

Here's a basic example to get started:

```python
from tamil_translite import translite

tam_sentence = "நிலையில்லாத இவ்வுலகில் நிலையானது தான் என்ன?"
translit_sentence = translite(tam_sentence)

print(translit_sentence)  # Output: nilaiyillaadha ivvulagil nilaiyaanadhu thaan enna?
```

