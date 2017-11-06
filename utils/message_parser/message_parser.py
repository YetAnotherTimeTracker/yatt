"""
Created by anthony on 15.10.17
message_parser
"""
import random


# TODO t-7-message-data-mining
def parse_message(message):
    return None


def parse_message_for_project(message):
    categories = ['personal', 'university', 'work', 'entertainment']
    return categories[random.randint(0, len(categories) - 1)]
