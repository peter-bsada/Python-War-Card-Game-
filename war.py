"""
My war file
"""

from deck import Deck
from hand import Hand

class War():
    """
    My war class
    """

    def __init__(self):
        self.player1 = Hand()
        self.player2 = Hand()
        self.deck = Deck()
        self.deck.create_card()
        self.deck.random_card()
        self.table = []
        print(self.split_card())


    def split_card(self):
        """
        Split half of the cards into player1 and player2
        """
        half = self.deck.split_list()
        hands1 = half[0]
        hands2 = half[1]
        self.player1.set_cards(hands1)
        self.player2.set_cards(hands2)



    def play_game(self):
        """
        My card game
        """
        while self.player1 > 0 and self.player2 > 0:
            player1_take_card = self.player1.take_card()
            player2_take_card = self.player2.take_card()

            print("player1 draws {}".format(player1_take_card))
            print("player2 draws {}".format(player2_take_card))

            self.table.append(player1_take_card)
            self.table.append(player2_take_card)

            print("\nPlayer 1:", len(self.player1.card))
            print("Player 2:", len(self.player2.card))
            print("list:", len(self.table))

            if player1_take_card.color == player2_take_card.color:
                if player1_take_card.number > player2_take_card.number:

                    for number in self.table:
                        self.player1 += number
                    self.table.clear()

                    print("\nplayer1 wins the round and picks up all cards.")
                    print("Status:")
                    print("Player 1:", len(self.player1.card))
                    print("Player 2:", len(self.player2.card))
                else:

                    for number in self.table:
                        self.player2 += number
                    self.table.clear()

                    print("player2 wins the round and picks up all cards.")
                    print("Status:")
                    print("Player 1:", len(self.player1.card))
                    print("Player 2:", len(self.player2.card))

            input("\nPress Enter to continue...\n")

        if self.player1 == 0:

            for number in self.table:
                self.player2 += number
            self.table.clear()

            print("player1 lost!")
            print("status:")
            print("player 1:", len(self.player1.card))
            print("player 2:", len(self.player2.card))
        else:

            for number in self.table:
                self.player1 += number
            self.table.clear()

            print("player2 lost!")
            print("status:")
            print("player 1:", len(self.player1.card))
            print("player 2:", len(self.player2.card))


if __name__ == "__main__":
    war = War()

    war.play_game()
