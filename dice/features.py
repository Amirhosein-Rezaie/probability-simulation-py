from enum import Enum
from tools.func import (
    select_outcome,
    show_result,
    total_repeat,
    count,
)
from random import randint
from numpy import var, std, mean, median


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
    __selected_face = None
    __total = 0
    __face_name = ""

    # methods
    def __init__(self):
        self.__selected_face = select_outcome(self.DiceOutcomes, "Dice")
        self.__total = total_repeat("Dice")
        self.__face_name = self.DiceOutcomes(self.__selected_face).name

    def specific_number(self):
        "Calculate posibability of a specific face of dice."

        if self.__selected_face not in [_ for _ in range(6)]:
            print("Invalid selected face for specific number test ... ")
            return 0

        outcomes = [randint(1, 6) for _ in range(self.__total)]

        probability = outcomes.count(self.__selected_face) / self.__total * 100
        theory = 1 / 6 * 100

        show_result(
            "Specific face (number)",
            self.__face_name,
            self.__total,
            probability,
            theory,
            abs(probability - theory),
            mean(outcomes),
            median(outcomes),
            var(outcomes),
            std(outcomes),
        )

    def even_number(self):
        "Calculate posibability of even number in many to dice."

        if self.__selected_face not in [_ for _ in range(7, 8 + 1)]:
            print("Invalid selected face for even or odd test ... ")
            return 0

        outcomes = [randint(1, 6) for _ in range(self.__total)]

        extperimental = 0
        if self.__selected_face == 7:
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
            self.__face_name,
            self.__total,
            extperimental,
            theoretical,
            abs(extperimental - theoretical),
            mean(outcomes),
            median(outcomes),
            var(outcomes),
            std(outcomes),
        )
