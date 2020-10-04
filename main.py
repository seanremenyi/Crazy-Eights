class Deck():
    cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K"]
    suits = ["♠", "♥", "♣", "♦"]
    deck = []        
            
    @classmethod
    def create_deck(cls):
        deck = []
        for value in cls.cards:
            for suit in cls.suits:
                cls.deck.append(value+suit)


class Hand()



new=Deck()
new.create_deck()
print(new.deck)