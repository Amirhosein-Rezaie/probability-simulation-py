from msvcrt import getwch
from tools.func import run_command, press_enter_to_continue, splitter_line


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

    len_sub_tests = {1: 1, 2: 4, 3: 4, 4: 4, 5: 1}
    sub_tests = {
        1: {
            "features": [
                "(1) Probability of (a outcome of single coin)",
            ]
        },
        2: {
            "features": [
                "(1) Exactly One (one specific outcome)",
                "(2) At Least One (one specific outcome)",
                "(3) All (one specific outcome)",
                "(4) All (one specific outcome)",
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


# run the function of the event or choice the user
def perform(test: int, sub_test: int) -> int:
    "run the function of the event or choice the user"

    # import modules of functions
    from coins.features import SingleCoin, MultipleCoin

    # list of functions
    funcs = {
        3: {1: None, 2: None, 3: None, 4: None},
        4: {1: None, 2: None, 3: None, 4: None},
        5: {1: None},
    }

    # make instance of classes and add functions in the dict
    instance = None
    if test == 1:
        instance = SingleCoin()
        funcs[1] = {1: instance.calculate_probability}
    elif test == 2:
        instance = MultipleCoin()
        funcs[2] = {1: instance.exactly_one, 2: None, 3: None, 4: None}

    splitter_line()

    funcs[test][sub_test]()

    splitter_line()


def main() -> None:
    "the main function of this project."

    while True:
        # clear the ternimal screen
        run_command(r"cls")

        number_test = list_tests()
        number_sub_test = list_sub_test(number_test)

        if number_sub_test == 0:
            continue

        perform(number_test, number_sub_test)

        press_enter_to_continue()


if __name__ == "__main__":
    main()
