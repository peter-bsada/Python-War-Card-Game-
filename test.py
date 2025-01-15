#!/usr/bin/env python3
# coding=utf8

""" Module for unittests """

import unittest
from hand import Hand
class Testcase(unittest.TestCase):
    """
    My test class
    """
    def test_gt(self):
        """
        test if other is greater than self.cards
        """
        gt = Hand().__gt__(-1)
        self.assertTrue(gt)

    def test_eq(self):
        """
        test if other is equal to self.cards
        """
        eq = Hand().__eq__(0)
        self.assertTrue(eq)

    def test_iadd(self):
        """
        add a number to self.card
        """
        iadd = Hand().__iadds__(52)
        self.assertListEqual(iadd, [52])

    def test_take_card(self):
        """
        test to pop out a number from a list
        """
        take_card = Hand().take_card_test()
        self.assertListEqual([take_card], [52])

    def test_set_cards(self):
        """
        add card to a list
        """
        set_cards = Hand().set_cards(52)
        self.assertListEqual([set_cards], [52])


if __name__ == '__main__':
    unittest.main(verbosity=3)
