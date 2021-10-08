from collections import Counter
from random import shuffle
from typing import Callable, Dict, List, Union


class Card:
    """ Card class
    definition:
    >>> c = Card('A', 'D')  # Diamond Ace
    
    Properties:
        number: value of the card ( from A to K )
        suit: suit of the card ( restricted values A, S, H or C )
    Methods:
        Getters are number and suits methods
        numbers and suits retruns the possible values
    """
    # static properties
    suits = {
        'D': {'symbol': '♢', 'value': 0.4},
        'S': {'symbol': '♠', 'value': 0.3},
        'H': {'symbol': '♡', 'value': 0.2},
        'C': {'symbol': '♣', 'value': 0.1}
    }
    numbers = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

    def __init__(self, number: Union[int, str], suit: str) -> None:
        if suit.upper() in Card.suits.keys():
            self.__suit = Card.suits[suit.upper()]
        else:
            raise ValueError('Unrecognized suit')
        if str(number).upper() in Card.numbers.keys():
            self.__number = number
        else:
            raise ValueError('Unrecognized card number')

    def __str__(self):
        return str(f"{self.__number}.{self.suits[self.__suit]['symbol']}")
    
    def __repr__(self):
        return str(self)
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Card):
            raise TypeError('Can only compare Cards')
        return str(self) == str(other)
        
    # protected properties
    number = property(fget=lambda self: self.__number)
    suit = property(fget=lambda self: self.__suit)


class Deck:
    """ Deck class - works as a stack
    Properties:
        __set: list of cards
    Methods:
        draw: pops one card from the deck
        reset: puts back all cards
        shuffle: reorder the deck ramdomly
    """
    main = tuple(Card(number=i, suit=n) for i in Card.numbers.keys() for n in Card.suits.keys())
    
    def __init__(self, n_decks: int = 1, values: Callable[[List[Card]], int] = None) -> None:
        """[summary]

        Args:
            n_decks (int, optional): number of normal decks to form the full deck
            Defaults to 1.
        """
        self.__n = n_decks
        self.__set = list()
        for _ in range(n_decks):
            self.__set += self.main
        
        self.__function = values if values is not None else (lambda lista: sum(c.numbers[c.number] + c.suits[c.suits] for c in lista))

    def __len__(self) -> int:
        return len(self.__set)
    
    @property
    def deck(self):
        return self.__set
    
    @property
    def value(self) -> int:
        return self.__function(self.__set)

    def shuffle(self) -> None:
        self.__init__()
        shuffle(self.__set)
        
    def sort(self, function: Callable[[List[Card]], int] = None) -> None:
        self.__set = sorted(self.__set, key=self.__function if function is None else function)        

    def reset(self) -> None:
        self.__init__(self.__n, self.__function)
    
    def add(self, value):
        if isinstance(value, Card):
            self.__hand.append(value)
        elif isinstance(value, Deck):
            self.__hand.extend(value.deck)
        else:
            raise TypeError('Can only add Cards or Decks')

    def draw(self) -> Card:
        return self.__set.pop(0)
    
    def remove(self, card: Card) -> None:
        """Remove specific cards in the deck

        Args:
            card (Card): card to be removed
        """
        self.__set.remove(card)
    
    def clear(self):
        self.__init__(0, self.__function)
    
    def count(self, card: Card = None) -> Union[int, Dict[Card, int]]:
        c = Counter(self.__set)
        if card is not None:
            return c[card]
        else:
            return {crd: c[crd] for crd in self.main}
