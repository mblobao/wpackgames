from wpackgames.pieces.cards import Card, Deck
from typing import Any, Union, Callable, List
from wpackgames.pieces.dices import Dice
from random import choice


class Player:
    """ Player class
    Properties:
        get_card: list of cards
    Methods:
        get_card: add card to players hand
        drop_card: remove card from players hand
        clear_hand: removes all cards from players hand
    """
    def __init__(self, name: str, npc: bool, deck_function: Callable[[List[Card]], int] = None) -> None:
        self.__name = name
        self.__hand = Deck(0, deck_function)
        self.__fun = deck_function
        self.__npc = npc
    
    def __repr__(self) -> str:
        return self.__name
    
    hand = property(fget=lambda self: self.__hand)
    name = property(fget=lambda self: self.__name)
    is_npc = property(fget=lambda self: self.__npc)
    
    @property
    def last_row(self) -> Any:
        pass
    
    @last_row.setter
    def last_row(self, value) -> None:
        pass
    
    def get_card(self, value: Union[Card, Deck], n: int = 1) -> None:
        if isinstance(value, Card):
            self.__hand.add(value)
        elif isinstance(value, Deck):
            for _ in range(n):
                self.__hand.add(value.draw())
        else:
            raise TypeError('Can only get Card or a Card from a Deck')
    
    def drop_card(self, card: Card = None, to: Deck = None):
        if card is None:
            self.__hand.remove(c := choice(self.__hand.deck))
        elif card not in self.__hand:
            raise IndexError(f"Card not in {self.__name}'s hand")
        else:
            self.__hand.remove(c := card)
        if to is not None:
            to.add(c)
        return c
    
    @staticmethod
    def roll_dices(*n, sum_: bool = False):
        result = [Dice(i).roll() for i in n]
        if sum_:
            return sum(result)
        return result

    def clear_hand(self) -> None:
        self.__hand = Deck(0, self.__fun)
