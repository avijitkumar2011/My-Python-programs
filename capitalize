#capitalize 
#To capitaze first letter of each word in string
def LetterCapitalize(str):

    x=str
    a=''
    flag=0
    for i in range(len(x)):
        if i==0:
            a=a+x[i].upper()
        elif x[i].isspace():
            flag=1
            a=a+x[i]
        elif flag==1:
            a=a+x[i].upper()
            flag=0
        else:
            a=a+x[i]
    return a

print (LetterCapitalize(input("enter a string")) )
