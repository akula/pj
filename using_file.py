#!/usr/bin/python
# Filename: using_file.python

poem = '''\
Programming is fun
when the work is done
if you wanna make your work as fun:
		using python
'''

f = open('poem.txt','w') #open the file
f.write(poem)
f.close

f = open('poem.txt')

while True:
	line = f.readline()
	if len(line) == 0:
		break
	print(line)
f.close()



