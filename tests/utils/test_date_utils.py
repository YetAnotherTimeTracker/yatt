"""
Created by anthony on 18.12.2017
test_date_utils
"""
import unittest

from datetime import datetime, date

import utils.date_utils as du


class TaskServiceTest(unittest.TestCase):

    def test_full(self):
        arg = '25 dec 03-30'
        parsed = du.parse_date_msg(arg)
        expected = datetime(year=date.today().year, month=12, day=25, hour=3, minute=30)
        self.assertEqual(parsed, expected)

    def test_full2(self):
        arg = '25 дек 13-37'
        parsed = du.parse_date_msg(arg)
        expected = datetime(year=date.today().year, month=12, day=25, hour=13, minute=37)
        self.assertEqual(parsed, expected)

    def test_only_time(self):
        arg = '03-30'
        parsed = du.parse_date_msg(arg)
        expected = datetime(year=date.today().year, month=date.today().month, day=date.today().day, hour=3, minute=30)
        self.assertEqual(parsed, expected)

    def test_only_time2(self):
        arg = '13:37'
        parsed = du.parse_date_msg(arg)
        expected = datetime(year=date.today().year, month=date.today().month, day=date.today().day, hour=13, minute=37)
        self.assertEqual(parsed, expected)

    # def test_day_and_time(self):
    #     arg = '15 03-30'
    #     parsed = du.parse_date_msg(arg)
    #     expected = datetime(year=date.today().year, month=date.today().month, day=15, hour=3, minute=30)
    #     if expected < datetime.now():
    #         expected = datetime(year=date.today().year, month=(date.today().month + 1) % 12, day=15, hour=3, minute=30)
    #
    #     self.assertEqual(parsed, expected)



if __name__ == '__main__':
    unittest.main()
