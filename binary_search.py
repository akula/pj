My_list = [1, 2, 3, 4, 5, 6, 7 , 8 , 9 , 10 , 11, 12]

def binary_search(find , list):
    low = 0
    high = len(list) - 1 
    
    while low <= high :
        m = (low + high)//2   
        if list[m] < find :
            low = m + 1
            print "now mid is %d "  % low
        elif list[m] > find :
            high = m
            print "now mid is %d"  % high
        else :
            print "now returning %d"  % m 
            return m
    return -1 
if __name__ == '__main__' :
    binary_search(9 , My_list)
    
