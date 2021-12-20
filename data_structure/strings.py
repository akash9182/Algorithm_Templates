import string

def string_operations():
    s = 'abcab'

    # join 
    print(','.join(s))

    # split
    print(s.split(','))

    # replace
    print(s.replace('aj', 'b'))

    # index, find 
    print(s.index('bc'))
    print(s.find('abb'))
    print(s.rfind('a'))
    
    # count
    print(s.count('a'))

    # start & end with
    
string_operations()