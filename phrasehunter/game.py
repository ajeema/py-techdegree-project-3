import random
import os

from .phrase import Phrase
from .artwork import *


class Game:
	"""The primary logic for the game"""

	def __init__(self, phrases):
		self.game_on = True
		self.phrases = [Phrase(phrase) for phrase in phrases]
		self.guessed_phrases_index = []

	# Make sure the user inputs valid options
	def fetch_guess(self, user_input):
		correct_guess = False

		self.cls()
		if len(user_input) > 1:
			print("Please input a single character only")
		elif not user_input.isalpha() and not user_input == " ":
			print("Please Input Only letters")
		elif user_input in self.guessed_char:
			print(f"You Have Already Tried {user_input}")
		elif not self.active_phrase.exists(user_input):
			print(f"We Couldn't Find {user_input} in The Phrase")

			# Show artwork depending on lives left
			self.life -= 1
			if self.life == 4:
				four_lives_left()
			elif self.life == 3:
				three_lives_left()
			elif self.life == 2:
				two_lives_left()
			elif self.life == 1:
				one_life_left()
			self.guessed_char.append(user_input)
		else:
			self.active_phrase.check_guess(user_input)
			self.guessed_char.append(user_input)
			correct_guess = True
		return correct_guess

	# Randomly select a phrase for play
	def current_phrase_picker(self):
		self.has_space = False
		self.current_index = random.randint(0, len(self.phrases) - 1)
		if len(self.guessed_phrases_index) == len(self.phrases):

			# Clearing The Guessed Array If Both Lengths are Same
			self.guessed_phrases_index = []
			for phrase in self.phrases:
				phrase.phrase_again()
		else:
			while self.current_index in self.guessed_phrases_index:
				self.current_index = random.randint(0, len(self.phrases) - 1)
		self.life = 5
		self.guessed_char = []
		self.active_phrase = self.phrases[self.current_index]
		if ' ' in self.active_phrase.phrase_:
			self.has_space = True

	def cls(self):
		os.system('cls' if os.name == 'nt' else 'clear')


	def run_game(self):
		self.cls()
		while self.game_on:
			print("This Is The Phrase Hunter Game!! Try Guessing The Phrase!!!")
			self.current_phrase_picker()

			while self.life:
				self.active_phrase.show_guessed_phrase()
				print(f"Lives Remaining: {self.life}")
				user_input = input("Guess One Character: ").upper()
				if self.has_space:
					# excuses white space so the user doesn't need to guess it
					correct_guess = self.fetch_guess(' ')
					correct_guess = self.fetch_guess(user_input)
				else:
					correct_guess = self.fetch_guess(user_input)
				if correct_guess:
					if self.active_phrase.entire_guessed():
						self.cls()
						print('Congrats!! You Won The Game!! You Were Able To Guess Whole Phrase...')
						self.active_phrase.show_guessed_phrase()
						self.guessed_phrases_index.append(self.current_index)
						# TODO - shouldn't use 4+ if's but it works for now...
						if self.restart_game() == False:
							break

				elif not self.life:
					self.cls()
					print("Sorry Cap'n, you're dead!")
					dead()
					print(f"The phrase was: {self.active_phrase.phrase_}")

					self.active_phrase.show_guessed_phrase()
					self.restart_game()
				else:
					continue

	def restart_game(self):

		while True:

			select_option = input("Would You Like To Play Again? [Y/N] : ")
			if select_option.upper() == 'Y':
				self.cls()
				self.current_phrase_picker()
				break
			elif select_option.upper() == 'N':
				self.game_on = False
				print("Thanks For Playing!!")
				return False
			else:
				self.cls()
				print("Sorry! Please type Y to play again or N to quit")
