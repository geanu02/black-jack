from Deck import Deck

class Player:

    def __init__(self, deck):
        self.player_hand = []
        self.player_deck = deck
        self.player_score = 0

    # Checks the current score of the player and returns the player_score
    def current_score(self):
        # Reset player score and loop through all of the player's cards
        self.player_score = 0

        # ace_counter checks if the card is an ace, and will determine if the card will
        # be equivalent to 1 or 11, depending on the current player score
        ace_counter = 0
        for _card in self.player_hand:
            # Ace points is defaulted to 11,
            # need to identify how many ace cards on player's hand
            if _card.card_points() == 11:
                ace_counter += 1
            # Calculate the rest of the points on player's hand
            else:
                self.player_score += _card.card_points()
        # The while loop determines if the current score is more than a "bust" which is > 21,
        # then the ace card drops to a score of 1 to continue the game
        while self.player_score > 21 and not ace_counter == 0:
            # Reduces the current score by 10 => 11 - 10 = 1
            self.player_score -= 10
            # breaks the loop when there is no more ace cards on the player's hand
            ace_counter -= 1
        return self.player_score
    
    def deal(self):
        # Draw 2 cards on first turn
        self.player_hand += self.player_deck.deck_draw(2)
        # Identify if 
        if self.current_score() == 21:
            return True
        return False

    # A hit allows the dealer to deal the Player one additional card.
    # Returns True if the Player's card is Bust, False if Player is still able to play.
    def hit(self):
        self.player_hand += self.player_deck.deck_draw(1)
        if self.current_score() > 21:
            return True
        return False
    
    def player_show(self):
        print("==================")
        print("Player's Cards")
        for _card in self.player_hand:
            _card.card_show()
        print(f"Player's Score: {self.player_score}")
        print("==================")