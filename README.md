# BanglaDictionary

BanglaDictionary is a Python package that provides a dictionary for the Bengali (Bangla) language. It allows you to retrieve meanings, pronunciations, examples, parts of speech, types, and sources of words in the Bengali language.

## Installation

You can install the BanglaDictionary package using pip:


## Usage

Here's an example of how to use the BanglaDictionary package:

```python
from BanglaDictionary import BanglaDictionary


# Create an instance of the BanglaDictionary
bd = BanglaDictionary()

# Get the meaning of a word
meaning = bd.get_meaning("আমি")
print(meaning)  # Output: "I"

# Get the pronunciation of a word
pronunciation = bd.get_pronunciation("আমি")
print(pronunciation)  # Output: "Ami"

# Get an example sentence for a word
example = bd.get_example("আমি")
print(example)  # Output: "আমি বাংলায় কথা বলি।"

# Get the part of speech (POS) of a word
pos = bd.get_pos("আমি")
print(pos)  # Output: "Pronoun"

# Get the type of a word
word_type = bd.get_type("আমি")
print(word_type)  # Output: "Personal Pronoun"

# Get the source of a word
source = bd.get_source("আমি")
print(source)  # Output: "Modern Bengali Dictionary"
```
```
# Get multiple meanings
meanings = bd.get_multiple_meanings("আমি", "খেলা", "বই")
print(meanings)  # Output: {"আমি": "I", "খেলা": "Game", "বই": "Book"}

# Get multiple pronunciations
pronunciations = bd.get_multiple_pronunciations("আমি", "খেলা", "বই")
print(pronunciations)  # Output: {"আমি": "Ami", "খেলা": "Khela", "বই": "Boi"}

# Get multiple examples
examples = bd.get_multiple_examples("আমি", "খেলা", "বই")
print(examples)  # Output: {"আমি": "আমি বাংলায় কথা বলি।", "খেলা": "তার খেলা খুব ভালোই ছিল।", "বই": "আমি একটি বই পড়ছি।"}

# Get multiple parts of speech (POS)
pos_list = bd.get_multiple_pos("আমি", "খেলা", "বই")
print(pos_list)  # Output: {"আমি": "Pronoun", "খেলা": "Noun", "বই": "Noun"}

# Get multiple types
types = bd.get_multiple_types("আমি", "খেলা", "বই")
print(types)  # Output: {"আমি": "Personal Pronoun", "খেলা": "Common Noun", "বই": "Common Noun"}

# Get multiple sources
sources = bd.get_multiple_sources("আমি", "খেলা", "বই")
print(sources)  # Output: {"আমি": "Modern Bengali Dictionary", "খেলা": "Online Bangla Dictionary", "বই": "Wiktionary"}
```

## Data Source

The data used by the BanglaDictionary package is sourced from Bangla Dictionary: Bangla Academy- ব্যবহারিক বাংলা অভিধান . The dictionary provides meanings, pronunciations, examples, parts of speech, types, and sources for a wide range of Bengali words.

## Contributing
If you find any issues or would like to contribute to the BanglaDictionary package, please feel free to open an issue or submit a pull request on the GitHub repository. You can contact via email: bip.sec22@gmail.com


## License
The BanglaDictionary package is released under the MIT License. You are free to use, modify, and distribute this package in your own projects.
