def coin(amount):
    m = [ 25 , 10 , 5 , 1]
    print "total amount is %d \n" % amount 
    for p in m :
        if  (amount//p) > 0 and amount%p != 0 :
            a = amount//p
            amount -= (amount//p)*p
            print "use %d pice of %d peny \2t " % ( a , p )
        elif (amount//p) > 0 and amount%p ==0 :
            b = amount//p
            print "use %d pcie of %d peng \n" % (b , p )
        else:
              continue
              
    