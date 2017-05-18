from readchar import readchar

from lib import get_game_list, count_levels

level = raw_input('Choose your level: 1, 2, 3, ...,' + str(count_levels()) + '\n')
game_list = get_game_list(int(level))
print 'Type the displayed letter!'

for i in game_list:
	print i
	while True:
		j = readchar()
		if j != i:
			print 'You typed ' + '"{}"'.format(j) + '. Try again to type '+'"{}"'.format(i)+'.'
		else:
			break

print 'Congratulations!!'
