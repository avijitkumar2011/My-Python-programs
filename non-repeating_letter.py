#To find the first non repeating letter in a string
x='aabbcbdce'
for i in x:
	count=0
	for j in x:
		if i==j:
			count=count+1
	if count==1:
		print(i)
		break
