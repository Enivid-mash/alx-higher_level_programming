#!/usr/bin/python3
'''
Module: 1-my_list
'''


class MyList(list):
    '''
    Represents a custom list called MyList
    '''
    def print_sorted(self):
        '''
        Prints the list in sorted order
        '''
        sorted_list = sorted(self)
        print(sorted_list)
