#!/usr/bin/env python3
import re
class MyString:
    def __init__(self, value=""):
        self.value = value

    @property
    def value(self):
        return self._value
    @value.setter
    def value(self, value):
        if isinstance(value, str):
            self._value = value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        x = self._value.endswith(".")
        return x
    
    def is_question(self):
        x = self._value.endswith("?")
        return x
    
    def is_exclamation(self):
        x = self._value.endswith("!")
        return x
    
    def count_sentences(self):

        sentences = re.split(r'[.?!]', self._value)
        print(f"{sentences}")
        
        i = 0
        length = len(sentences)
        while i < length:
            if sentences[i] == "":
                sentences.remove(sentences[i])
                i -= 1
                length -= 1
            i += 1

        count = len(sentences)

        print(f"{count}")
        return count


