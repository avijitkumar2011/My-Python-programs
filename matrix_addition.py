x=[[1,2,3],
   [4,5,6],
   [7,8,9]]
y=[[11,22,33],
   [14,12,13],
   [90,80,60]]
z=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(len(x)):
	for j in range(len(x[0])):
		z[i][j]=x[i][j]+y[i][j]
for i in range(len(x)):
	print(z[i])

