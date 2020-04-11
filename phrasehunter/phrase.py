import random

from character import Character


class Phrase():
    current_letter_index = []

    def __init__(self, phrase):
        self.phrase = phrase
        self.character_phrase = Character(self.phrase)

    def check_possibility(self):
        if self.character_phrase.was_guessed == False:
            dummy_array = []

            for l in self.phrase:
                dummy_array.append(l)
            for i in dummy_array:
                if self.phrase == i:
                    self.current_letter_index.append(dummy_array.index(i))
                    print(self.current_letter_index)

    # def __iter__(self):
    #     yield from self.phrase

    def entire_guessed(self):
        glist = []
        for self.letter in self.phrase:
            if self.letter.was_guessed:
                glist.append(self.letter)

            if len(glist) == len(self.current_phrase):
                return True


