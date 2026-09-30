from msvcrt import getwch
from tools.func import run_command


# the function that show list of tests and user select one of them.
def list_tests() -> int:
    "the function that show list of tests and user select one of them."

    print("""
        (1) Coin Toss Probability
        (2) Multiple Coin Toss
        (3) Dice Roll Probability
        (4) Two Dice Sum Probability
        (5) Monte Carlo Pi Estimation
        """)

    # try to get number of test
    number = 0
    print("Enter the number of one test : ", flush=True, end="")
    while True:
        try:
            char = int(getwch())

            if char >= 1 and char <= 5:
                print(char)
                number = char
                break
        except:
            pass

    return number


# function that show the list on sub_tests of tests and select one of them.
def list_sub_test(test_number: int) -> int:
    "function that show the list on sub_tests of tests and select one of them."


def main() -> None:
    "the main function of this project."

    # clear the ternimal screen
    run_command(r"cls")

    number_test = list_tests()


if __name__ == "__main__":
    main()
