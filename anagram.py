#To check if two strings are anagrams or not
x='mean'
y='name'
def sorting(z):
	p1=sorted(z)
	return p1
x1=sorting(x)
y1=sorting(y)
if x1==y1:
	print('anagram')
else:
	print('not anagram')

