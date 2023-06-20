#!/usr/bin/python3
import unittest
from models.base import Base


'''
Creating test cases for the base module
'''


class TestBase(unittest.TestCase):
    '''
    Testing base
    '''

    def test_id_none(self):
        '''
        Test case: Sending no id
        '''
        b = Base()
        self.assertEqual(1, b.id)

    def test_id(self):
        '''
        Test case: Sending a valid id
        '''
        b = Base(50)
        self.assertEqual(50, b.id)

    def test_id_zero(self):
        '''
        Test case: Sending an id of 0
        '''
        b = Base(0)
        self.assertEqual(0, b.id)

    def test_id_negative(self):
        '''
        Test case: Sending a negative id
        '''
        b = Base(-20)
        self.assertEqual(-20, b.id)

    def test_id_string(self):
        '''
        Test case: Sending an id that is not an int (a string)
        '''
        b = Base("Betty")
        self.assertEqual("Betty", b.id)

    def test_id_list(self):
        '''
        Test case: Sending an id that is not an int (a list)
        '''
        b = Base([1, 2, 3])
        self.assertEqual([1, 2, 3], b.id)

    def test_id_dict(self):
        '''
        Test case: Sending an id that is not an int (a dictionary)
        '''
        b = Base({"id": 109})
        self.assertEqual({"id": 109}, b.id)

    def test_id_tuple(self):
        '''
        Test case: Sending an id that is not an int (a tuple)
        '''
        b = Base((8,))
        self.assertEqual((8,), b.id)
