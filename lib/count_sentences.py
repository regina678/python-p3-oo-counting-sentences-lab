#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = ""
        self.value = value  # Use setter to apply validation

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self._value.endswith(".")

    def is_question(self):
        return self._value.endswith("?")

    def is_exclamation(self):
        return self._value.endswith("!")

    def count_sentences(self):
        import re
        # Split on ., !, or ? followed by a space or end of string
        split_sentences = re.split(r'[.!?]', self._value)
        # Remove empty strings and whitespace-only strings
        return len([s for s in split_sentences if s.strip()])

