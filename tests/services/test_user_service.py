"""
Created by anthony on 25.10.17
user_service_test.py
"""
import unittest
# from unittest.mock import MagicMock
# from mock import patch
#from services.user_service import find_one_by_username


class UserServiceTest(unittest.TestCase):

    # @patch('services.user_service.find_all')
    def test_find_one_by_username(self):
        self.assertEquals(1, 1)


if __name__ == '__main__':
    unittest.main()
