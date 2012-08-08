#!/usr/bin/python
# Filename: objvar.py

class Person:
    '''Pepresents person'''
    population = 0

    def __init__(self,name):
        '''Initializes the person data.'''
        self.name = name
        print("initializing %s" %self.name)
        Person.population += 1
        

    def __del__(self):
        ''' I am dying.'''
        print("%s say bye" % self.name)

        Person.population -= 1

        if Person.population == 0 :
            print("I am the last one .")
        else:
            print("There are still %d person left" % Person.population)

    def sayHi(self):
        print("Hi my name is %s" % self.name)




    def howmany(self):
        if Person.population == 1:
            print("I am the only person here")
        else:
            print("We have %d person here" % Person.population)



ale = Person('ale')
ale.sayHi()
ale.howmany()


jijinger = Person('jijinger')
jijinger.sayHi()
jijinger.howmany()

ale.sayHi()
ale.howmany()
