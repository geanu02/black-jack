from Deck import Deck
from Player import Player
from Dealer import Dealer

class Blackjack:

    def __init__(self):
        self.deck = Deck(shuffle=True)
        self.player = Player(self.deck)
        self.dealer = Dealer(self.deck)
        self.game_play()

    def ending_score(self):
        if self.dealer.current_score() > self.player.current_score():
            print("Dealer wins! Sorry, you lose!")
        elif self.dealer.current_score() < self.player.current_score():
            print("You win the game! Nice job!")
        else:
            print("It's a tie! Hope you enjoyed the game!")

    def game_play(self):
        # Player.deal method draws two cards, and returns a bool value
        deal_player = self.player.deal()
        deal_dealer = self.dealer.deal()

        # Shows the player's hand
        self.player.player_show()

        # CHECKING IF YOU WIN THROUGH BLACKJACK OR TIE IF BOTH THROUGH BLACKJACK 

        # Tie if the player and the dealer get Blackjack
        if deal_player == deal_dealer == True:
            print("You and the Dealer got Blackjack! It's a tie!")
            return
        # If the first turn the player gets Blackjack,
        # then the player wins and the game ends
        elif deal_player == True and deal_dealer == False:
            print("You win the game! You got Blackjack!")
            return
    
        # ========== PLAYER'S TURN ===========

        _input = None
        # Looping while 
        while not _input == "stand":
            _bust = False
            _input = input("Hit or Stand? ").lower()

            if _input == "hit":
                # Player.hit method returns True if the score goes over 21 which is a BUST,
                # and will end the game. False will continue the game.
                _bust = self.player.hit()
                # Shows the player's hand after hitting
                self.player.player_show()
            if _bust == True:
                print("Player is busted! Sorry, you lose!")
                return
            
        # ========== DEALER'S TURN ===========

        # Shows the dealer's hand after hitting
        self.dealer.player_show()

        # CHECKING IF THE DEALER WINS THROUGH BLACKJACK

        if deal_dealer == True:
            print("Dealer got Blackjack! Sorry, you lose!")
            return
        
        # I read online if the dealer's current score is greater than 17,
        # it does not deal any more cards
        while self.dealer.current_score() <= 17:
            # Player.hit method returns True if the score goes over 21 which is a BUST,
            # and will end the game. False will continue the game.
            if self.dealer.hit() == True:
                self.dealer.dealer_show()
                print("Dealer is busted! You win!")
                return
            else:
                self.dealer.dealer_show()

        self.ending_score()

gian = Blackjack()