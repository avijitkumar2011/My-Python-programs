#To sort the list elements
x=[24,54,15,42,7,98]
n=len(x)
for i in range(n):
	for j in range(0,n-i-1):
		if x[j] > x[j+1]:
			x[j],x[j+1]=x[j+1],x[j]
print(x)
