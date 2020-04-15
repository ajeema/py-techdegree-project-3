
# artwork from https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c#file-hangmanwordbank-py
def full_life():
	print('''   
	=========
	  +---+
	  |   |
	      |
	      |
	      |
	      |
	=========''')

def four_lives_left():
	print('''   
	=========
	  +---+
	  |   |
	  O   |
	      |
	      |
	      |
	=========''')

def three_lives_left():
	print('''   
	=========
	  +---+
	  |   |
	  O   |
	 /|   |
	      |
	      |
	=========''')

def two_lives_left():
	print('''   
	=========
	  +---+
	  |   |
	  O   |
	 /|\  |
	      |
	      |
	=========''')

def one_life_left():
	print('''   
	=========
	  +---+
	  |   |
	  O   |
	 /|\  |
	 /    |
	      |
	=========''')

def dead():
	print('''   
	=========
	  +---+
	  |   |
	  O   |
	 /|\  |
	 / \  |
	      |
	=========''')

