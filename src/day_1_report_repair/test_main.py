import unittest
from unittest.mock import patch

from src.day_1_report_repair.main import report_repair, report_repair_three_numbers


class Test(unittest.TestCase):


    def test_report_repair(self):
        data  = [1721, 979, 366, 299, 675, 1456]
        # the two numbers that sum upt to 2020 are 1721 & 299
        expected = 1721 * 299

        actual = report_repair(data)

        self.assertEqual(expected, actual)


    def test_report_repair_edge_cases(self):
        self.assertEqual(report_repair([]), 0, "empty data should return 0")
        self.assertEqual(report_repair([1]), 0, "data containing only 1 item should return 0")
        self.assertEqual(report_repair([0, 2020]), 0, "it should return 0 if one of the terms is 0")
        self.assertEqual(report_repair([1, 2, 3]), 0, "when there are no a,b: a+b=2020 return 0")
        self.assertEqual(report_repair([-1, 2021]), -2021, "it should be able to work with negative inputs")

        # invalid data inputs
        self.assertEqual(report_repair(["1", "2"]), 0, "it should fail non integer data")
        self.assertEqual(report_repair([[1], [2]]), 0, "it should reject poorly structured data")
        self.assertEqual(report_repair("123456"), 0, "it should reject poorly structured iterables")

    @patch('builtins.print')
    def test_report_repair_with_invalid_data_input(self, mocked_print):
        self.assertEqual(report_repair(["1", 2, [3]]), 0, "should reject poorly structured data")
        mocked_print.assert_called_with("Error: expected data to be of type list[int]")


    def test_report_repair_three_numbers(self):
        data = [1721, 979, 366, 299, 675, 1456]
        # the three numbers that sum upt to 2020 are 979 & 366 & 675
        expected = 241861950

        actual = report_repair_three_numbers(data)

        self.assertEqual(expected, actual)


    def test_report_repair_three_numbers_edge_cases(self):
        self.assertEqual(report_repair_three_numbers([]), 0, "empty data should return 0")
        self.assertEqual(report_repair_three_numbers([1]), 0, "data containing only one item should return 0")
        self.assertEqual(report_repair_three_numbers([0, 2020, 0]), 0, "it should return 0 if two of the terms is 0")
        self.assertEqual(report_repair_three_numbers([1, 2, 3]), 0, "when there are no a,b,c: a+b+c=2020 return 0")
        self.assertEqual(report_repair_three_numbers([-1, -2, 2023]), 4046, "it should be able to work with negative inputs")


    def test_report_repair_three_numbers_with_invalid_data_inputs(self):
        self.assertEqual(report_repair_three_numbers(["1", "2", "3"]), 0, "it should fail non integer data")
        self.assertEqual(report_repair_three_numbers([[1], [2], [3]]), 0, "it should reject poorly structured data")

        # mixed data types should raise type Errors
        self.assertRaises(TypeError, report_repair_three_numbers, *["1", 2, [3]])



if __name__ =='__main__':
    unittest.main()
