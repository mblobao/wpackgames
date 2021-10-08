from random import randint
from typing import List, Union

class Dice:
    def __init__(self, sides: int = 6) -> None:
        self.__sides = sides
    
    def roll(self) -> int:
        return randint(1, self.__sides)
    
    def n_roll(self, n: int) -> List[int]:
        return [self.roll() for _ in range(n)]
            

class DiceGroup:
    def __init__(self, *dices) -> None:
        self.__dices = list()
        for d in dices:
            if isinstance(d, Dice):
                self.__dices.append(d)
            elif isinstance(d, int):
                self.__dices.append(Dice(d))
            else:
                raise TypeError('All parameters must be instances of Dice')
        self.__dices = tuple(self.__dices)
    
    def roll(self, sum_: bool = False) -> Union[int, List[int]]:
        rolls = list(d.roll() for d in self.__dices)
        if sum_:
            return sum(rolls)
        return rolls
