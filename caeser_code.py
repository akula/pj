import string
import sys


def decode(tr):
    start = 'a';
    end = 'z';

    startnum = ord(start)
    endnum = ord(end) + 1
    src = ''

    for i in xrange(startnum, endnum):
        src = src + chr(i)
    
    
    for drift in range(1,26):
        new_src=''
        for i in src:
            new_src = new_src + chr((ord(i) - 97 + drift) % 26 + 97 )

        leet = string.maketrans(src,new_src)
        print tr.translate(leet)
        print '\n'