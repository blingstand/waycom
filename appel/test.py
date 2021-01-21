#! /usr/bin/python3
from io import StringIO
import os, sys
import unittest
from unittest.mock import patch, MagicMock

from .worker import Worker

path = os.path.dirname(__file__)
if path not in sys.path: 
    sys.path.insert(0, path)

class TestWorker(unittest.TestCase):
    """The TestWorker class, it is triggered by pytests"""
    
    @patch("sys.stdin", StringIO("1 2 3\n4 5 6")) #need this to init Worker() and build w
    def test_get_input_text(self):
        """this function tests if get_input_text returns stdin without line break"""
        w = Worker()
        self.assertEqual(w.plain_text, "1 2 3 4 5 6")

    @patch("sys.stdin", StringIO("1 2 3\n4 5 6"))
    def test_convert_to_list(self):
        """this function tests if we get the 2 same lists from w.plain_text input"""
        w = Worker()
        w.plain_text = "123:456 789:147"
        self.assertEqual(w.plain_text, "123:456 789:147")
        a, b = w.convert_to_list()
        self.assertEqual(a, [123, 147, 456, 789]) #sorted list of numbers asc
        self.assertEqual(b, [(123, 456), (789, 147)]) #list of pairs 


    @patch("sys.stdin", StringIO("1 2 3\n4 5 6"))
    def test_peak_call_1_highest_peak(self):
        """ this function tests if we get a 1 point highest peak with w.converted_to_list input"""
        w = Worker()
        w.converted_to_list = [1,2,4,5], [(1,2), (4,5)]
        highest_peak = w.peak_call
        self.assertEqual(highest_peak, 1)

    @patch("sys.stdin", StringIO("1 2 3\n4 5 6"))
    def test_peak_call_2_highest_peak(self):
        """ this function tests if we get a 2 points highest peak with w.converted_to_list input"""
        w = Worker()
        w.converted_to_list = [1,2,3,5], [(1,3), (2,5)]
        highest_peak = w.peak_call
        self.assertEqual(highest_peak, 2)



