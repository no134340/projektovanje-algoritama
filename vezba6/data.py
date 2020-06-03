"""
DESCRIPTION:
    Character data class.
"""


class Data:

    def __init__(self, val, freq):
        self.value = val
        self.frequency = freq

    def __repr__(self):
        return f'{self.value} : {self.frequency}'
