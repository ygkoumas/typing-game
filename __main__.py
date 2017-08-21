from readchar import readchar

from lib import get_game_list, count_levels

level_count = count_levels()
while True:
	try:
		level_message = 'Choose your level: 1, 2, 3, ...,{}\n'.format(level_count)
		level = int(raw_input(level_message))
		if level <= level_count and level > 0:
			break
		else:
			print 'Number should be between 1 and {}.'.format(level_count)
	except ValueError:
		print 'That was no valid number. Try again.'


game_list = get_game_list(int(level))
print 'Type the displayed letter!'

for i in game_list:
	print i
	while True:
		j = readchar()
		if j == i:
			break
		elif j == '\x03':
			raise KeyboardInterrupt
		elif j == '\x04':
			raise EOFError
		else:
			print 'You typed "{}". Try again to type "{}".'.format(j, i)

print 'Congratulations!!'
