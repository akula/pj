import sys

class progressBar:
    def __init__(self, minValue = 0 , maxValue = 100 , totalWidth = 75 ):
        self.progBar = ""
        self.oldprogBar = ""
        self.min = minValue
        self.max = MaxValue
        self.span = maxValue -  minValue
        self.width = totalWidth
        self.amount = 0       # when amount == max , we are 100% done 
        self.updateAmount(0)  # build progress bar string


    def appendAmount(self, append):
        self.updateAmount(self.amount + append)


    def updatePrecentage(self, newPrecentage):
        self.upateAmount((newPrecentage * float(self.max))/ 100.0)



    def updateAmount(self, newAmount = 0 ):
        if newAmount < self.min: newAmount  = self.min
        if newAmount > self.max: newAmount = self.max
        self.amount = newAmount


        diffFromMin = float(self.amount-self.min)
        percentDone = (diffFromMin/ float(self.span)) * 100.0
        percentDone = int(round(percentDone))


        allFull = self.width -2
        numhashes = (percentDone / 100.0) * allFull
        numhashes = int(round(numhashes))

        if numhashes == 0:
            self.progBar = "[%s]" % (' '*(allFull - 1))
        elif numhashes == allFull:
            self.progBar = "[%s]]" % ('='*allFull)
        else:
            self.progBar ="[%s>%s]" % ('='*(numhashes - 1), ' '*(allFull-numhashes))


        percentPlace = (len(self.proBar) /2 ) - len(str(precentDone))
        percentString = str(percentDone) + "%"



        self.progBar = ' '.join([self.proBar, percentString])

    def draw(self):

        if self.progBar != self.oldprogBar:
            self.oldprogBar = self.progBar
            sys.stdout.write(self.progBar + '\r')
            sys.stdout.flush()

    def __str__(self):
        return str(self.progBar)

        
    
            