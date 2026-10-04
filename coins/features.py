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
            self.__outcome_name,
            self.__total_repeate,
            probability,
            50,
            difference,
            mean_outcomes,
            median_outcomes,
            variance_outcomes,
            std_outcomes,
        )


class MultipleCoin:
    # # properties
    __number_coin = 0
    __outcome = None
    __outcome_name = ""
    __total_repeat = 0

    # # functions
    def __get_number_coin(self) -> int:
        while True:
            try:
                number = int(input("Enter Number of coins : "))

                if number >= 1:
                    return number
                else:
                    print("Enter number greater or equal 1 ... !")

            except ValueError:
                print("Enter the number for number coins ... !")

    def __get_tests(self, number_test: int, number_in_test: int) -> list:
        "Function for get outcome of a coin in 2D list"
        tests = []
        for _ in range(number_test):
            tests.append([randint(0, 1) for _ in range(number_in_test)])
        return tests

    def __replace_in_list(self, list: list) -> list:
        "replace 1 and 0 with True and False in list"

        return [1 if item is True else 0 for item in list]

    # # methods
    def __init__(self):
        self.__total_repeat = total_repeat("Flip a coin")
        self.__number_coin = self.__get_number_coin()
        self.__outcome = select_outcome(SingleCoin.Coin, "coin")
        self.__outcome_name = SingleCoin.Coin(self.__outcome).name

    def exactly_one(self) -> int:
        "calculate the probability of an outcome that should happend one time in every tests"

        # gets the outcomes
        tests = self.__get_tests(self.__total_repeat, self.__number_coin)

        # get numbers of tests that excatly have one specific outcome
        count_test = sum(test.count(self.__outcome) == 1 for test in tests)

        # check which test in tests have exactly one specific outcome
        result = [test.count(self.__outcome) == 1 for test in tests]
        result = self.__replace_in_list(result)

        # calculate and show the result
        theory = (self.__number_coin / 2**self.__number_coin) * 100
        probability = count_test / self.__total_repeat * 100
        show_result(
            f"Multiple Coin Toss (Exactly one {self.__outcome_name})",
            self.__outcome_name,
            self.__total_repeat,
            probability,
            theory,
            abs(probability - theory),
            mean(result),
            median(result),
            var(result),
            std(result),
        )

    def least_one(self):
        "Calculate the probability of getting a specific outcome at least once in each experiment"

        # gets the outcomes
        tests = self.__get_tests(self.__total_repeat, self.__number_coin)

        # get numbers of tests that have at least one specific outcome
        count_test = sum(test.count(self.__outcome) >= 1 for test in tests)

        # check which test in tests have exactly one specific outcome
        result = [test.count(self.__outcome) >= 1 for test in tests]
        result = self.__replace_in_list(result)

        # calculate and show the result
        theory = (1 - (1 - 0.5) ** self.__number_coin) * 100
        probability = count_test / self.__total_repeat * 100
        show_result(
            f"Multiple Coin Toss (At least one {self.__outcome_name})",
            self.__outcome_name,
            self.__total_repeat,
            probability,
            theory,
            abs(probability - theory),
            mean(result),
            median(result),
            var(result),
            std(result),
        )
