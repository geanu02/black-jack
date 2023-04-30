from Deck import Deck
from Player import Player

class Dealer(Player):

    def __init__(self, deck):
        super().__init__(deck)

    def dealer_show(self):
        print("==================")
        print("Dealer's Cards")
        for _card in self.player_hand:
            _card.card_show()
        print(f"Dealer's Score: {self.player_score}")
        print("==================")