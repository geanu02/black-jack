class Card:

    card_type = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suit_type = ['Heart', 'Diamond', 'Club', 'Spade']

    def __init__(self, value, suit):
        # Card Value is the point equivalence of the card
        # Deck.deck_build uses range(1, 14) to make sure the points are correct
        self.card_value = value
        # Card Face is the face type of the card (e.g. Ace, 5, 9, Jack, etc.)
        # Deck.deck_build uses range(1, 14) and [value - 1] becomes the correct index for card_type
        self.card_face = self.card_type[value - 1]
        # Card Suit is the suit type of the card (e.g. Hearts, Clubs, etc.)
        self.card_suit = self.suit_type[suit]

    def card_show(self):
        print(f"{self.card_face} of {self.card_suit}s")

    def card_points(self):
        _pts = 0
        # If Card is Ace, default its point equivalence to 11
        if self.card_value == 1:
            _pts = 11
        # If Card is 10, Jack, Queen or King, default its point equivalence to 10
        elif self.card_value >= 10:
            _pts = 10
        # Everything else, default its point equivalence to its card number
        else:
            _pts = self.card_value 
        return _pts