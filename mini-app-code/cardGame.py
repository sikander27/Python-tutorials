import pdb
import collections
import random
PlayingCard = collections.namedtuple('card', ['suit', 'rank'])


class PlayingDeck:
    ranks = [str(rank) for rank in range(2, 11)] + ['J', 'O', 'K', 'A']
    suits = ['Spades', 'Diamonds', 'Hearts', 'Clubs']

    def init(self):
        self._cards = [PlayingCard(rank, suit)
                       for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]


# if __name__ == '_main_':
deck = PlayingDeck()
pdb.set_trace()
# 1. Slicing a deck
first_cut = deck[:4]
# 2. Iterating through a deck for card in deck:
for card in deck:
    print(card)
# 3. Iterating through the deck in reverse for card in reversed (deck):
for card in reversed(deck):
    print(card)
# 4. Shuffling the deck
shuffled_deck = random.shuffle(deck)
for card in shuffled_deck:
    print(card)
