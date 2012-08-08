def checkio_strip(line):
    s = []
    for i in line.split(' '):
        if i == '' :
            continue
        else:
            s.append(i)
    return ' '.join(s)
    
