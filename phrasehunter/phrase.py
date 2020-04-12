from .character import Character


class Phrase:
    current_letter_index = []

    def __init__(self, phrase):
        self.phrase = phrase
        self.character_phrase = Character(self.phrase)

    def check_possibility(self):
        if self.character_phrase.was_guessed is False:
            return True
        else:
            return False

    """def __iter__(self):
                    yield from self.phrase"""


    def entire_guessed(self):
        glist = []
        for self.letter in self.phrase:
            if self.letter.was_guessed:
                glist.append(self.letter)
            if len(glist) == len(self.current_phrase):
                return True
