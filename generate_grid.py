import random


def get_int(msg, minmum, defalut):
    while True:
        try:
            line = input(msg)
            if not line and defalut is not None:
                return defalut
            i = int(line)
            if i < minmum:
                print("must be >=", minimum)
            else:
                return i
        except ValueError as err:
            print(err)

rows = get_int("rows:", 1, None)
columns = get_int("columns:",1,None)
minimum = get_int("minimum (or Enter for 0)",-1000, 0)

defalut = 1000
if defalut < minimum:
    defalut = 2*minimum
maximum = get_int("maximum (or Enter for" +str(defalut) +":)", minimum, defalut)

row = 0
while row < rows:
    line = ""
    column = 0
    while column <columns:
        i = random.randint(minimum, maximum)
        s = str(i)
        while len(s) <10 :
            s = " " + s
            line += s
            column += 1
        print(line)
        row += 1
        
            
    
