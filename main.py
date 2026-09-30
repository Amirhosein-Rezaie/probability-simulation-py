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

    len_sub_tests = {1: 2, 2: 4, 3: 4, 4: 4, 5: 1}
    sub_tests = {
        1: {
            "features": [
                "(1) Probability of Heads",
                "(2) Probability of Tails",
            ]
        },
        2: {
            "features": [
                "(1) Exactly One Head",
                "(2) At Least One Head",
                "(3) All Heads",
                "(4) All Tails",
            ]
        },
        3: {
            "features": [
                "(1) Specific Number",
                "(2) Even Number",
                "(3) Odd Number",
                "(4) Number Greater Than 4",
            ]
        },
        4: {
            "features": [
                "(1) Sum Equals to (a number)",
                "(2) Sum Is Even",
                "(3) Sum Is Odd",
                "(4) Sum Is Greater Than (a number)",
            ]
        },
        5: {"features": ["(1) Monte Carlo Pi Estimation"]},
    }

    # select 0 for going back
    print("\n" + "\t\t" + "(0) Go back")

    # show sub_tests
    for sub_test in sub_tests[test_number]["features"]:
        print("\t\t" + sub_test)

    # choice a sub test
    number = 0
    print("\n" + "Enter the number of one sub test : ", flush=True, end="")
    while True:
        try:
            char = int(getwch())

            if repr(char) >= repr(0) and repr(char) <= repr(len_sub_tests[test_number]):
                print(char)
                number = char
                break
        except:
            pass

    return number


def main() -> None:
    "the main function of this project."

    while True:
        # clear the ternimal screen
        run_command(r"cls")

        number_test = list_tests()
        number_sub_test = list_sub_test(number_test)

        if number_sub_test == 0:
            continue


if __name__ == "__main__":
    main()
