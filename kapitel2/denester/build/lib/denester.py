'''
This is the modul "denester.py". It provides a function called printnl()
to print a nested list which can contain any amount of embedded lists.
'''
def printnl(a_list, level):
    '''
    this function has one argument named "a_list", which takes any python
    list (with optionally embedded lists). The elements of the list will
    be printed out recursive. Each element will be printed out one per line.
    With the second argument "level" tabs could be included in embedded lists.
    '''
    for element in a_list:
        if isinstance(element, list):
            printnl(element, level+1)
        else:
            for tabs in range(level):
                print('\t', end='')
            print(element, level)
