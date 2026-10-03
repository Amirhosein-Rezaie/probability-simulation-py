from tools.func import total_repeat, select_outcome, count
from enum import Enum
from random import randint


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
        outcomes = []

        for _ in range(self.__total_repeate):
            outcomes.append(randint(0, 1))

        result = count(outcomes, [1, 0])

        print(result)

        print(result[1] / self.__total_repeate * 100)
