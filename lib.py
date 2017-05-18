from random import shuffle

LETTERS_LENGTH = 30

def get_game_list(level):
	letters = []
	for i in range(level):
		letters += level_map[i]
	letters = letters * int(LETTERS_LENGTH/len(letters))
	shuffle(letters)
	return letters

def count_levels():
	return len(level_map)

level_map = [
	['j', 'f'],
	['d', 'k'],
	['s', 'l'],
	['a', ';'],
	['g', 'h'],
	['r', 'u'],
	['e', 'i'],
	['w', 'o'],
	['q', 'p'],
	['t', 'y'],
	['m', 'v'],
	[',', 'c'],
	['x', '.'],
	['z', '/'],
	['b', 'n'],
]
