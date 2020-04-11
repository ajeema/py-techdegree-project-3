import random


from phrase import Phrase

class Game:
	life = 5
	underscores = []

	def __init__(self, phrases):
		self.phrases = phrases
		self.input_phrase = Phrase(self.phrases)
		self.stored_phrases = ['Have a Nice Day', 'We Are Having Fun', 'You Can Win', 'Keep Going Forward', 'Be Grateful']
		self.current_phrase = self.stored_phrases[int(random.randint(0, len(self.phrases) -1 ))]

	def create_board(self):
		for i in array:
			new_element = '_ ' * len(i)
			new_element = new_element[0:-1]
			self.underscores.append(new_element)

	def print_board(self):
		array = self.current_phrase.split(' ')

		current_board = ''
		for j in self.underscores:
			current_board += j + ' '

		return self.underscores
game1 = Game('b')
print(game1.print_board())
