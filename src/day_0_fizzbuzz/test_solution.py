from io import StringIO

import unittest
from unittest.mock import patch

from .solution import fizzbuzz

class MyTestCase(unittest.TestCase):

    @patch("builtins.print")
    def test_fizzbuzz_with_invalid_n(self, mocked_print):
        fizzbuzz(0)
        fizzbuzz(-1)
        mocked_print.assert_not_called()

        # wrong data type
        self.assertRaises(TypeError, fizzbuzz, "10")

    @patch("builtins.print")
    def test_fizzbuzz_with_1(self, mocked_print):
        fizzbuzz(1)
        mocked_print.assert_called_with(1)

    @patch("sys.stdout", new_callable=StringIO)
    def test_fizzbuzz_with_2(self, mocked_stdout):
        fizzbuzz(2)
        expected = "1\n" \
                   "2\n"
        self.assertEqual(expected, mocked_stdout.getvalue())

    @patch("sys.stdout", new_callable=StringIO)
    def test_fizzbuzz_with_3(self, mocked_stdout):
        fizzbuzz(3)
        expected = "1\n" \
                   "2\n" \
                   "Fizz\n"
        self.assertEqual(expected, mocked_stdout.getvalue())


    @patch("sys.stdout", new_callable=StringIO)
    def test_fizzbuzz_with_5(self, mocked_stdout):
        fizzbuzz(5)
        expected = "1\n" \
                   "2\n" \
                   "Fizz\n" \
                   "4\n" \
                   "Buzz\n"
        self.assertEqual(expected, mocked_stdout.getvalue())


    @patch("sys.stdout", new_callable=StringIO)
    def test_fizzbuzz_with_15(self, mocked_stdout):
        fizzbuzz(15)
        expected = "\n".join([
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz"
        ])
        self.assertEqual(expected, mocked_stdout.getvalue().rstrip("\n"))



if __name__ == '__main__':
    unittest.main()
