from enum import Enum
from msvcrt import getwch
from tools.func import (
    select_outcome,
    show_result,
    total_repeat,
    count,
)
from random import randint
from numpy import var, std, mean, median
from itertools import product


class Dice:
    # inner classes
    class DiceOutcomes(Enum):
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5
        six = 6
        Odd_numbers = 7
        Even_numbers = 8

    # properties
    selected_face = None
    total = 0
    face_name = ""

    # methods
    def __init__(self):
        self.selected_face = select_outcome(self.DiceOutcomes, "Dice")
        self.total = total_repeat("Dice")
        self.face_name = self.DiceOutcomes(self.selected_face).name

    def specific_number(self):
        "Calculate posibability of a specific face of dice."

        if self.selected_face not in [_ for _ in range(1, 6 + 1)]:
            print("Invalid selected face for specific number test ... ")
            return 0

        outcomes = [randint(1, 6) for _ in range(self.total)]

        probability = outcomes.count(self.selected_face) / self.total * 100
        theory = 1 / 6 * 100

        show_result(
            "Specific face (number)",
            self.face_name,
            self.total,
            probability,
            theory,
            abs(probability - theory),
            mean(outcomes),
            median(outcomes),
            var(outcomes),
            std(outcomes),
        )

    def even_number(self):
        "Calculate posibability of even or odd number in many to dice."

        if self.selected_face not in [_ for _ in range(7, 8 + 1)]:
            print("Invalid selected face for even or odd test ... ")
            return 0

        outcomes = [randint(1, 6) for _ in range(self.total)]

        extperimental = 0
        if self.selected_face == 7:
            extperimental = (
                len([n for n in outcomes if n % 2 != 0]) / len(outcomes) * 100
            )
        else:
            extperimental = (
                len([n for n in outcomes if n % 2 == 0]) / len(outcomes) * 100
            )

        theoretical = 1 / 2 * 100

        show_result(
            "Even or Odd Face (Number)",
            self.face_name,
            self.total,
            extperimental,
            theoretical,
            abs(extperimental - theoretical),
            mean(outcomes),
            median(outcomes),
            var(outcomes),
            std(outcomes),
        )

    def greater_than(self):
        "Calculate posibability of greater that an specific number or face."

        if self.selected_face not in [_ for _ in range(1, 6 + 1)]:
            print("Invalid selected face for greater than a number test ... ")
            return 0

        # want greater than or greater that equeal
        flag_gte = False
        print("Do you to calculate with n >= o ? (y:n) ", flush=True, end="")
        while True:
            char = getwch()
            if char in ["y", "n"]:
                print(char)
                flag_gte = True if char == "y" else False
                break

        # calculate
        outcomes = [randint(1, 6) for _ in range(self.total)]

        extperimental = theoretical = 0

        if flag_gte:
            extperimental = (
                len([n for n in outcomes if n >= self.selected_face])
                / len(outcomes)
                * 100
            )
            theoretical = (
                len([_ for _ in range(1, 6 + 1) if _ >= self.selected_face]) / 6 * 100
            )
        else:
            extperimental = (
                len([n for n in outcomes if n >= self.selected_face])
                / len(outcomes)
                * 100
            )
            theoretical = (
                len([_ for _ in range(1, 6 + 1) if _ >= self.selected_face]) / 6 * 100
            )

        show_result(
            f"Greater Than or Equal To ({self.selected_face})",
            self.face_name,
            self.total,
            extperimental,
            theoretical,
            abs(extperimental - theoretical),
            mean(outcomes),
            median(outcomes),
            var(outcomes),
            std(outcomes),
        )


class MultipleDice(Dice):
    number_dice = 0

    # # functions
    def __get_test_number(self) -> int:
        while True:
            try:
                number = int(input("Enter target Number : "))

                if number >= 1:
                    return number
                else:
                    print("Enter number greater or equal 1 ... !")

            except ValueError:
                print("Invalid input ... !")

    def __get_number(self) -> int:
        while True:
            try:
                number = int(input("Enter Number of dice : "))

                if number >= 1:
                    return number
                else:
                    print("Enter number greater or equal 1 ... !")

            except ValueError:
                print("Enter the number for number dice ... !")

    def __init__(self):
        super().__init__()
        self.number_dice = self.__get_number()

    def sum_equals(self):
        "calculate the posibability of sum of the dices equals to a number"

        # simulation the test
        outcomes = []

        for i in range(self.total):
            outcomes.append([randint(1, 6) for j in range(self.number_dice)])

        # cal the sun of outcomes
        sum_outcomes = [sum(test) for test in outcomes]

        target_number = self.__get_test_number()

        # filter the outcomes
        count_equals = len([s for s in sum_outcomes if s == target_number])

        # # calculate the posibability
        extperimental = count_equals / len(sum_outcomes) * 100

        # theory
        true_outcomes = list(product(range(1, 7), repeat=self.number_dice))

        count_theoretical = len(
            [sum(outcome) for outcome in true_outcomes if sum(outcome) == target_number]
        )

        theoretical = count_theoretical / (6**self.number_dice) * 100

        # show result
        show_result(
            f"Sum multiple Dice equals to ({target_number})",
            "none",
            self.total,
            extperimental,
            theoretical,
            abs(extperimental - theoretical),
            mean(sum_outcomes),
            median(sum_outcomes),
            var(sum_outcomes),
            std(sum_outcomes),
        )
