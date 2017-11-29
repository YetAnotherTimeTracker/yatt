"""
Created by denis 
date_test
"""
import unittest
import datetime


class DateParserTests(unittest.testCase):
    def test(self):

        text = "21 дек 13-37"
        expectation = datetime.of(2017 - 12 - 21 - 13:37: 00)
        reality = service_utils.parseDate(text)
        self.assertEquals(expectation, reality)

    def test2(self):

        text = "21 дек 13 37"
        expectation = dateTime.of(2017 - 12 - 21 - 13:37: 00)
        reality = service_utils.parseDate(text)
        self.assertnotEquals(expectation, reality)


if __name__ == '__main__':
    unittest.main()
