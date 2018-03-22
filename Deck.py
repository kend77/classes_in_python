from Card import Card
from random import shuffle


class Deck:
    def __init__(self):
        self.cards = [Card(suit, value)
                      for suit in Card.suits for value in Card.values]

    def count(self):
        return len(self.cards)

    def __repr__(self):
        return f"Deck of {len(self.cards)} cards"

    def _deal(self, num):
        removed_cards = []
        if not len(self.cards):
            return ValueError("All cards have been dealt")
        while num > 0 and len(self.cards):
            removed_cards.append(self.cards.pop())
            num -= 1
        return removed_cards

    def shuffle(self):
        if len(self.cards) == 52:
            return shuffle(self.cards)
        return ValueError("Only full decks can be shuffled")

    def deal_card(self):
        return self._deal(1)

    def deal_hand(self, num):
        return self._deal(num)
