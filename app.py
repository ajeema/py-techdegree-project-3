from phrasehunter.game import Game
from phrasehunter.constants import stored_phrases


if __name__ == '__main__':
	game = Game(stored_phrases)
	try:
		game.run_game()
	except KeyboardInterrupt:
		print("\nThanks for playing!")
