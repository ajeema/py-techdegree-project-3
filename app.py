from phrasehunter.game import Game

from phrasehunter.constants import STORED_PHRASES



if __name__ == '__main__':
	game = Game(STORED_PHRASES)
	game.run_game()