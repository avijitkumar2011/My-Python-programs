#To count no. of vovel in the given string
x = 'This is my first line in python'
y = 'aeiou'
for ch in y:
	c=0
	for k in x:
		if ch == k:
			c = c+1
	print(ch+':', c)
