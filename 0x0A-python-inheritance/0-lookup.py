#!/usr/bin/python3
'''
This is a function that returns the list of attributes of an object.
'''


def lookup(obj):
    '''
    Function: lookup()
    Returns a list object containing the attributes of the input object.
    '''
    return dir(obj)
