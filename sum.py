def checkio_sum(value):
    sum = 0
    for i in value:
        sum += i
    return sum


if __name__== '__main__' :
    results = checkio_sum([1,2,3,4,5])
    print('a[1,2,3,4,5] sum result is', results)
    
