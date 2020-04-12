"""
original_phrases = ['Have A Nice Day', 'We Are Having Fun', 'You Can Win', 'Keep Going Forward', 'Be Grateful']
self.current_phrase = self.original_phrases[int(random.randint(0, len(self.original_phrases)))]

"""
import random

from .phrase import Phrase


class Game:
	life = 5
	underscores = []
	stored_phrases = ['Have A Nice Day', 'We Are Having Fun', 'You Can Win', 'Keep Going Forward', 'Be Grateful']
	current_phrase = stored_phrases[int(random.randint(0, len(stored_phrases) - 1))]

	def __init__(self, phrases):
		self.phrases = phrases
		self.input_phrase = Phrase(self.phrases)

		print('Current Phrase = ' + self.current_phrase)

	def create_board(self, needed_phrase):
		array = self.current_phrase.split(' ')

		for i in array:
			new_element = ''
			for j in i:
				if needed_phrase != "0" and (j.lower() == needed_phrase or j == needed_phrase.upper()):
					new_element += j + ' '

				else:
					new_element += '_ '

			self.underscores.append(new_element)

	def print_board(self):

		if self.input_phrase.check_possibility() is True:
			true_phrase = self.input_phrase.phrase
			self.create_board(true_phrase)

		current_board = ''
		for i in self.underscores:
			current_board += i + '  '
		return current_board

	def run_game(self):
		print(self.print_board() + '\n')
		while self.life > 0:
			user_input = input('Enter Your Guess: ')
			self.__init__(user_input)
			print(self.print_board() + '\n')
