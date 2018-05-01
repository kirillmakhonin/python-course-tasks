import sys
import unittest
from unittest.mock import patch
import io
mocked_stdin = """\
0
0
0
3
4
0
"""

#@patch('builtins.input', side_effect=mocked_stdin.split())
@patch(target='builtins.input', side_effect=lambda : '0')
class TestInput(unittest.TestCase):
    
    def test_valid_input(self, *args):
        print(args)
        self.assertEqual(input(), '0')
