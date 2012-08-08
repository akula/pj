#!/usr/bin/python2
#Filename: pickling.py

import pickle

#the name of the file where we will store the object

shoplistfile = 'shoplist.data'

shoplist = ['apple','mango','carrot']

f = open(shoplistfile, 'wb')

pickle.dump(shoplist,f)
f.close()

del shoplist

f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)

