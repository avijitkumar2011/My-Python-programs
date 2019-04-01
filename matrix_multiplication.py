m1=[[0,0,0],
    [0,0,0],
    [0,0,0]]
m2=[[0,0,0],
    [0,0,0],
     [0,0,0]]
m3=[[0,0,0],
   [0,0,0],
   [0,0,0]]
for i in range(0,3):
    for j in range(0,3):
        m1[i][j]=int(input("enter a number"))

for i in range(0,3):
        print(m1[i])

for i in range(0,3):
    for j in range(0,3):
        m2[i][j]=int(input("enter a number"))

for i in range(0,3):
        print(m2[i])
sum =0
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            sum = sum + m1[i][k] * m2[k][j]
        m3[i][j] = sum
        sum = 0

print("matrix multiplication :")
for i in range(0,3):
        print(m3[i])
