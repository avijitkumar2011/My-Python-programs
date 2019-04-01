#To print different combinations of three numbers
x=[3,5,8]
for i in range(0,3):
	for j in range(0,3):
		for k in range(0,3):
			if i != j and j != k and i != k :
				print(x[i],x[j],x[k])
