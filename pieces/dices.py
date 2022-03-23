from random import randint, random
from scipy.stats import binom


def coin_toss(p: float = 0.5) -> bool:
    if not isinstance(p, float):
        raise TypeError('')  # TODO: Value Error Text
    if not (0 < p < 1):
        raise ValueError('')  # TODO: Value Error Text
    return float(random()) < p
    

class Dice:
    def __init__(self, sides: int = 6) -> None:
        self.__sides = sides
    
    def roll(self, n: int = 1) -> int:
        if not isinstance(n, int):
            raise TypeError
        elif n < 1:
            raise ValueError('')
        elif n == 1:
            return randint(1, self.__sides)
        else:
            return [randint(1, self.__sides) for _ in range(n)]
    
    def __add__(self, other: object) -> list[int]:
        if isinstance(other, type(self)):
            return [self.roll(), other.roll()]
        elif isinstance(other, list):
            if all([isinstance(o, type(self)) for o in other]):
                other.append(self.roll())
                return other
            else:
                raise TypeError('')
        else:
            raise TypeError('')
    
    def __radd__(self, other: object) -> list[int]:
        return self + other
    
    def __mul__(self, integer: int) -> list[int]:
        return self.roll(integer)
    
    def __rmul__(self, integer: int) -> list[int]:
        return self.roll(integer)
    
    def probability(self, n: int = 1) -> float:
        pass
            

def dice_probability(self, sizes: int, n: int, successes: int, greater_than: int) -> float:
    p = 1 - greater_than / sizes
    return binom.sf(k=successes, n=n, p=p)
