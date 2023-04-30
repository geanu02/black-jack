from Card import Card
from random import randint

class Deck:

    def __init__(self, shuffle=True):
        self.deck_cards = []
        self.deck_shuffle(shuffle)

    # Returns the number of cards
    def deck_count(self):
        return len(self.deck_cards)
    
    # Builds the deck of 52 cards
    def deck_build(self):
        for _value in range(1, 14):
            for _suit in range(0, 4):
                self.deck_cards.append(Card(_value, _suit))

    # This class method calls the deck_build and shuffles the deck_cards using the for loop below
    def deck_shuffle(self, shuffle):
        if shuffle:
            self.deck_build()
            for idx in range(len(self.deck_cards) - 1, 0, -1):
                rdx = randint(0, idx)
                self.deck_cards[rdx], self.deck_cards[idx] = self.deck_cards[idx], self.deck_cards[rdx]

    # This class method removes a card/cards from the deck_cards according to how many 
    # is on the parameter 'times', and returns a list of those drawn cards
    def deck_draw(self, times):
        cards_drawn = []
        for idx in range(times):
            chosen_card = self.deck_cards.pop()
            cards_drawn.append(chosen_card)
        return cards_drawn