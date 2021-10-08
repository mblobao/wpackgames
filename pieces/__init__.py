from wpackgames.pieces.cards import Card, Deck
from wpackgames.pieces.dices import DiceGroup
from typing import Union, Callable, List
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
        self.__npc = npc
    
    def __repr__(self) -> str:
        return self.__name
    
    hand = property(fget=lambda self: self.__hand)
    name = property(fget=lambda self: self.__name)
    is_npc = property(fget=lambda self: self.__npc)
    
    @property
    def hand(self) -> Deck:
        return self.__hand
    
    def get_card(self, value: Union[Card, Deck]) -> None:
        if isinstance(value, Card):
            self.__hand.add(value)
        elif isinstance(value, Deck):
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
        return c
    
    def roll_dices(*n, sum_: bool = False):
        return DiceGroup(*n).roll
