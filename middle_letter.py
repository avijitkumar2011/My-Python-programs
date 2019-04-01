#To find middle letter in a string
def middle(strg):
	if len(strg) % 2 == 1:
		n = len(strg)//2
		print('Middle letter in string is:', strg[n])
	else:
		print('enter string of length odd number')


middle('kuma')
