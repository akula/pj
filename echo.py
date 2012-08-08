import string

def checkio_echo(str1):
    a=[]
    test = str1.replace(' ','')
    n = len(test)
    for i in  range(len(test)//2) :
        if test[i] != test[n-i-1]:
            return -1

    return 0
