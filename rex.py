import string

def checkio_query(str):
    query , index = str.split(';')

    for source in query.split(','):
        re1, partitiion, re2 = source.partition(':')
        if re1 == index :
            return re2   
