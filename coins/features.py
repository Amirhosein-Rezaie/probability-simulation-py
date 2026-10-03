from tools.func import total_repeat, select_outcome, count, show_result
from enum import Enum
from random import randint
from numpy import mean, median, var, std


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

        # calcaulate
        probability = result[1] / self.__total_repeate * 100
        difference = abs(probability - 50)
        mean_outcomes = mean(outcomes)
        variance_outcomes = var(outcomes)
        std_outcomes = std(outcomes)
        median_outcomes = median(outcomes)

        # show the result
        show_result(
            "Single Coin",
            self.Coin(self.__outcome),
            self.__total_repeate,
            probability,
            50,
            difference,
            mean_outcomes,
            median_outcomes,
            variance_outcomes,
            std_outcomes,
        )
