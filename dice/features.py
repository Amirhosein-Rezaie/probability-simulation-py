from enum import Enum
from tools.func import select_outcome, show_result, total_repeat, count
from random import randint
from numpy import var, std, mean, median


class Dice:
    # inner classes
    class DiceFaces(Enum):
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5
        six = 6

    # properties
    __selected_face = None
    __total = 0
    __face_name = ""

    # methods
    def __init__(self):
        self.__selected_face = select_outcome(self.DiceFaces, "Dice")
        self.__total = total_repeat("Dice")
        self.__face_name = self.DiceFaces(self.__selected_face).name

    def specific_number(self):
        outcomes = [randint(1, 6) for _ in range(self.__total)]

        print(outcomes)

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
