"""
Description:
    Hash table data module.
Author:
    Jasmina Savić RA40/2017
"""


class Data:

    def __init__(self, key):
        self.key = key
        self.literal = str(key)

    def __repr__(self):
        return f'{self.key}'