"""
Created by denis 
date_test
"""
import unittest
import datetime


class DateParserTests:
    def test(self):

        text = "21 дек 13-37"
        # expectation = datetime.of(2017-12-21-13:37:00)
        # reality = service_utils.parseDate(text)
        # self.assertEquals(expectation, reality)

    def test2(self):

        text = "21 дек 13 37"
        # expectation = datetime.of(2017-12-21-13:37:00)
        # reality = service_utils.parseDate(text)
        # self.assertnotEquals(expectation, reality)

    def test3(self):
        text = "221 дек 13:37"
        # expectation = datetime.of('error')
        # reality = service_utils.parseDate(text)
        # self.assertEquals(expectation, reality)

    def test4(self):
        text = "21 дик 13 37"
        # expectation = datetime.of(2017-12-21-13:37:00)
        # reality = service_utils.parseDate('error')
        # self.assertnotEquals(expectation, reality)

    def test5(self):
        text = "21 дек "
        # expectation = datetime.of(2017-12-21-00:01:00)
        # reality = service_utils.parseDate('error')
        # self.assertnotEquals(expectation, reality)

    def test6(self):
        text = "21 дек 133-37"
        # expectation = dateTime.of(2017-12-21-133:37: 00)
        # reality = service_utils.parseDate('error')
        # self.assertnotEquals(expectation, reality)


if __name__ == '__main__':
    unittest.main()
