import unittest

from main import report_repair, report_repair_three_numbers


class Test(unittest.TestCase):

    def setUp(self) -> None:
        with open("resources/day1_input_data") as f:
            # read data and cast to integers
            self.testData = list(map(int, f.readlines()))


    def test_report_repair(self):
        data  = [1721, 979, 366, 299, 675, 1456]
        # the two numbers that sum upt to 2020 are 721 & 299
        expected = 514579 # 721 * 299

        actual = report_repair(data)

        self.assertEqual(expected, actual)


    def test_report_repair_with_puzzle_input(self):
        #print(report_repair(self.testData))
        self.assertEqual(report_repair(self.testData), 691771)


    def test_report_repair_three_numbers(self):
        data = [1721, 979, 366, 299, 675, 1456]
        # the three numbers that sum upt to 2020 are 979 & 366 & 675
        expected = 241861950

        actual = report_repair_three_numbers(data)

        self.assertEqual(expected, actual)


    def test_report_repair_three_numbers_with_puzzle_input(self):
        # print(report_repair_three_numbers(self.testData))
        self.assertEqual(report_repair_three_numbers(self.testData), 232508760)


if __name__ =='__main__':
    unittest.main()
