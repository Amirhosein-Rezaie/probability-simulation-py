from tools.func import total_repeat, select_outcome
from enum import Enum


class SingleCoin:
    class Coin(Enum):
        Heads = 0
        Tails = 1

    __total_repeate = 0
    __outcome = None
    __outcome_name = ""

    def __init__(self):
        self.__total_repeate = total_repeat("Flip a coin")
        self.__outcome = select_outcome(self.Coin, "coin")
        self.__outcome_name = self.Coin(self.__outcome).name

    def show(self):
        print(self.__outcome_name)
        print(self.__total_repeate)

    def calculate_probability(self):
        pass
