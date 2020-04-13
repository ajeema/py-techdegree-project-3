from .character import Character


class Phrase:
    current_letter_index = []

    def __init__(self, phrase):
        self.phrases = [Character(letter) for letter in phrase]


    def entire_guessed(self):
        for letter in self.phrase:
            if letter.was_guessed:
                return False
        return True

    def show_guessed_phrase(self):
        for letter in self.phrases:
            print(letter.show_single_character(), end=' ')
            print('a')
