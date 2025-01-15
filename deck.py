
"""
My deck file
"""

import random
from card import Card

class Deck():
    """
    innehåller 52 blandade kortlek
    """

    def __init__(self):
        self.list = []

    def create_card(self):
        """
        create all my cards
        """
        for color in range(0, 4):
            for  number in range(0, 13):
                self.list.append(Card(number, color))
        return self.list

    def random_card(self):
        """
        Shuffle my cards
        """
        random.shuffle(self.list)

    def split_list(self):
        """
        split my cards in  half
        """
        half = len(self.list)//2
        return self.list[:half], self.list[half:]
