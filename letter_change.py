#To increase the order of each alphabet by one and if it is a vovel then capitalize it, in a alphanumeric string
def LetterChanges(str):

    x=str
    a=''
    b=''
    for i in x:
        if i.isalpha():
            a=a+chr(ord(i)+1)
        else:
            a=a+i
    for j in a:
        if j in ['a','e','i','o','u','A','E','I','O','U']:
            b=b+j.upper()
        else:
            b=b+j


    return b


print (LetterChanges(input("enter a string")))  
