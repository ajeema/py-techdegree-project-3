class Character:

    guessed_list = []
    was_guessed = False
    number = ['0','1','2','3','4','5','6','7','8','9']
    is_number = False

    def __init__(self, char):
        char = char.upper()
        for i in str(char):
            if i in self.number:
                self.is_number = True
            else:
                continue
        if self.is_number == True:
            raise ValueError("please enter a string not a number")
        else:
            if len(char) == 1:
                if char in self.guessed_list:
                    self.was_guessed = True
                else:
                    self.char = char
                    self.guessed_list.append(self.char)
            else:
                raise ValueError("Please enter one letter at a time")

