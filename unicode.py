def c():
    '''
     str->str
     converts string to its unicode
     >>>hello
     72 101 108 108 111
    '''
    strng=input('enter the string: ')
    for ch in strng:
        print(ord(ch),end=' ')
    return
