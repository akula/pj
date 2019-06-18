#!/use/bin/python2
# Filename:cat.py


import sys
def readline(filename):
    '''print a file to the standard output'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line, #notice comma
    f.close()

#Script starts from here
if len(sys.argv) < 2 :
    print 'No action specified.'
    sys.exit()

if sys.argv[1].startswith('-'):
    option = sys.argv[1][2:]
    #fetch sys.argv[1] but without hte first two characters
    if option == 'version':
        print 'Version 12.2'
    elif option == 'help':
        print '''\
        This programm prints files to the standard output.
        any number of files can be specified.
        options include:
        --version
        --help :Display this help'''

    else:
        print 'Unknow option.'
        sys.exit()
else:
    for filename in sys.argv[1:]:
        readline(filename)
