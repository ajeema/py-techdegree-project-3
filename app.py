from phrasehunter.game import Game
from phrasehunter.constants import stored_phrases


if __name__ == '__main__':
	game = Game(stored_phrases)
	game.run_game()