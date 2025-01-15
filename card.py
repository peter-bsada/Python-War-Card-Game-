"""
My card file
"""
class Card():
    """
    för mina kort
    """

    value = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    colors = ["hjärta", "spader", "ruter", "klöver"]

    def __init__(self, number, color):
        self.number = number
        self.color = color

    def __repr__(self):
        """
        my repr function
        """
        return "{} {}".format(self.value[self.number], self.colors[self.color])
