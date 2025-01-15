"""
hand file
"""

# from deck import Deck

class Hand():
    """
    My deck class
    """

    def __init__(self):
        self.card = []

    def set_cards(self, cards):
        """
        My set_cards function
        """
        self.card = cards
        return self.card

    def take_card(self):
        """
        my take_card function
        """
        return self.card.pop()

    def __gt__(self, other):
        """
        my gt function
        """
        if len(self.card) > other:
            return True
        return False

    def __eq__(self, other):
        """
        My eq function
        """
        if len(self.card) == other:
            return True
        return False

    def __iadd__(self, other):
        """
        my iadd function
        """
        self.card.append(other)
        return self

    def __iadds__(self, other):
        """
        my iadd function for test
        """
        self.card.append(other)
        return self.card

    def take_card_test(self):
        """
        my take_card function
        """
        self.card = [52]
        return self.card.pop()
