### buble sorting

def buble_sorting(list):
    for i in range(0,len(list) - 1):
        for j in range(0 , len(list) -1):
            if list[j] >= list[j+1]:
                list[j] , list[j+1] = list[j+1] , list[j]
        print list



        