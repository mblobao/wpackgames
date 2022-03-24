from collections import Counter
from random import shuffle
from typing import Any, Callable, Union


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
    __suits = {
        'D': {'symbol': '♢', 'value': 0.4},
        'S': {'symbol': '♠', 'value': 0.3},
        'H': {'symbol': '♡', 'value': 0.2},
        'C': {'symbol': '♣', 'value': 0.1}
    }
    __numbers = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13}

    def __init__(self, number: Union[int, str], suit: str) -> None:
        if suit.upper() in Card.suits.keys():
            self.__suit = Card.suits[suit.upper()]
        else:
            raise ValueError('Unrecognized suit')
        if str(number).upper() in Card.numbers.keys():
            self.__number = number
        else:
            raise ValueError('Unrecognized card number')

    def __str__(self) -> str:
        return str(f"{self.__number}.{self.suits[self.__suit]['symbol']}")
    
    def __repr__(self) -> str:
        return f'{self.__name__} {self}'
    
    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Card):
            raise TypeError('Can only compare Cards')
        return self.value == other.value
    
    def __ne__(self, other: Any) -> bool:
        if isinstance(other, Card):
            raise TypeError('Can only compare Cards')
        return self.value != other.value
    
    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Card):
            raise TypeError('Can only compare Cards')
        return self.value > other.value
    
    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Card):
            raise TypeError('Can only compare Cards')
        return self.value >= other.value
    
    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Card):
            raise TypeError('Can only compare Cards')
        return self.value < other.value
    
    def __le__(self, other: Any) -> bool:
        if isinstance(other, Card):
            raise TypeError('Can only compare Cards')
        return self.value <= other.value
    
    # protected properties
    number = property(fget=lambda self: self.__number)
    suit = property(fget=lambda self: self.__suit)
    
    @property
    def value(self) -> float:
        crd = str(self).split('.')
        return self.numbers[crd[0]] + self.suits[crd[1]]['value']


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
    
    def __init__(self, n_decks: int = 1, values: Callable[[list[Card]], int] = None) -> None:
        """[summary]

        Args:
            n_decks (int, optional): number of normal decks to form the full deck
            Defaults to 1.
            
            values: (Callable, optional): function that calculates the Deck value
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

    def shuffle(self, n: int = 1) -> None:
        self.__init__()
        for _ in range(n):
            shuffle(self.__set)
        
    def sort(self, function: Callable[[list[Card]], int] = None) -> None:
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

    def draw(self, n: int = 0) -> Card:
        return self.__set.pop(n)
    
    def remove(self, card: Card) -> None:
        """Remove specific cards in the deck

        Args:
            card (Card): card to be removed
        """
        self.__set.remove(card)
    
    def clear(self):
        self.__init__(0, self.__function)
    
    def count(self, card: Card = None) -> Union[int, dict[Card, int]]:
        c = Counter(self.__set)
        if card is not None:
            return c[card]
        else:
            return {crd: c[crd] for crd in self.main}
