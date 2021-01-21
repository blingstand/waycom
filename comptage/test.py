#! /usr/bin/python3
from io import StringIO
import os, sys
import unittest
from unittest.mock import patch, MagicMock

try:    
    from worker import Worker 
except ModuleNotFoundError:
    from .worker import Worker

path = os.path.dirname(__file__)
if path not in sys.path: 
    sys.path.insert(0, path)

class TestWorker(unittest.TestCase):
    """The TestWorker class, it is triggered by pytests"""

    @patch("sys.stdin", StringIO("1 2 3\n\n\n4 5 6")) #need this to init Worker() and build w
    def test_get_input_text(self):
        """this function tests if get_input_text returns stdin without line break"""
        w = Worker()
        self.assertEqual(w.plain_text, "1 2 3   4 5 6")

    @patch("sys.stdin", StringIO("abg\n [{|}]# \n4 5 6 eno"))
    def test_remove_non_accepted(self):
        """this function tests if the non_accepted char from input has been removed """
        w = Worker()
        self.assertEqual(w.pure_text, 'abg  #     eno')
        self.assertEqual(w.split_input, ["abg", "#", "eno"])
    
    @patch("sys.stdin", StringIO("abg\n [{|}]# \n4 5 6 eno"))
    def test_display_answer(self):
        """this function tests if the non_accepted char from input has been removed """
        w = Worker()
        w.split_input = ["foo", "bar", "baz", "foo"]
        a = "2 : foo\n1 : bar\n1 : baz\n"
        self.assertEqual(w.display_answer, a)
