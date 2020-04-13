"""
original_phrases = ['Have A Nice Day', 'We Are Having Fun', 'You Can Win', 'Keep Going Forward', 'Be Grateful']
self.current_phrase = self.original_phrases[int(random.randint(0, len(self.original_phrases)))]

"""
import random

from .phrase import Phrase


class Game:

	def __init__(self, phrases):
		self.game_on = True
		self.phrases = [Phrase(phrases) for phrases in phrases]
		self.life = 5

	def current_phrase_picker(self):
		self.current_phrase = self.phrases[random.randint(0, len(self.phrases))]

	def run_game(self):
		c = 0
		while self.game_on:
			print("This is the Phrase Hunter Game!! Try Guessing the Phrase!!")
			while self.life < 5:
				c += 1
				self.current_phrase.show_guessed_phrase()
			self.game_on = False







































#
# class Game:
# 	life = 5
# 	underscores = []
# 	stored_phrases = ['Have A Nice Day', 'We Are Having Fun', 'You Can Win', 'Keep Going Forward', 'Be Grateful']
# 	current_phrase = stored_phrases[int(random.randint(0, len(stored_phrases) - 1))]
#
# 	def __init__(self, phrases):
# 		self.phrases = phrases
# 		self.input_phrase = Phrase(self.phrases)
#
# 		print('Current Phrase = ' + self.current_phrase)
#
# 	def create_board(self, needed_phrase):
# 		array = self.current_phrase.split(' ')
#
# 		for i in array:
# 			new_element = ''
# 			for j in i:
# 				if needed_phrase != "0" and (j.lower() == needed_phrase or j == needed_phrase.upper()):
# 					new_element += j + ' '
#
# 				else:
# 					new_element += '_ '
#
# 			self.underscores.append(new_element)
#
# 	def print_board(self):
#
# 		if self.input_phrase.check_possibility() is True:
# 			true_phrase = self.input_phrase.phrase
# 			self.create_board(true_phrase)
#
# 		current_board = ''
# 		for i in self.underscores:
# 			current_board += i + '  '
# 		return current_board
#
# 	def run_game(self):
# 		print(self.print_board() + '\n')
# 		while self.life > 0:
# 			user_input = input('Enter Your Guess: ')
# 			# TODO make it only take a life if that letter has not been guessed or incorrect.
# 			self.life -= 1
#
# 			self.__init__(user_input)
# 			print(self.print_board() + '\n')
# 			print(f"you have {self.life} out of 5 lives left")
# 			print('''You have guessed these letters: ''',
# 				  Character.guessed_list)
