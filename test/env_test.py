"""
Created by anthony on 15.10.17
env_test
"""
import os


def test_env_var():
    assert os.environ['BOT_ENV'] == 'development'
