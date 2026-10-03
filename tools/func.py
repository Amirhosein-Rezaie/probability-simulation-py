from subprocess import run
from msvcrt import getwch
from enum import Enum
from unittest import result


# run a commant in terminal
def run_command(command: str) -> None:
    if command:
        run(f"{command}", shell=True)


# function for pressing enter key to continue
def press_enter_to_continue() -> None:
    "function for pressing enter key to continue"

    print("Press enter to continue ... ", flush=True, end="")

    while True:
        char = getwch()

        if repr(char) == repr("\r"):
            break


# function for show a splitter line
def splitter_line(len_line: int = 60) -> None:
    "show a splitter line"

    print("-" * len_line)


# get the total repeat of one event
def total_repeat(event: str) -> int:
    "get the total repeat of one event"

    total = 0
    while True:
        try:
            total = int(input(f"Enter the total repeate for {event} event : "))

            break

        except ValueError:
            print("Please enter total repeat as a number ... \n")

    return total


# show the outcomes of a thing
def select_outcome(outcomes: Enum, thing: str):
    "show and select outcomes of a thing"

    print(f"Select outcomes of {thing} ... ")

    # variables
    values = []

    for outcome in outcomes:
        print(f"({outcome.name}) {outcome.value}")
        values.append(outcome.value)

    # select one of them
    print(
        f"Enter the number of outcome [{values[0]},{values[-1]}]: ",
        end="",
        flush=True,
    )
    while True:
        try:
            char = int(getwch())

            if char in values:
                print(char)
                return char
        except:
            pass


# count the items in a list of outcomes
def count(list_outcomes: list, outcome_names: list) -> dict:
    "count the items in a list of outcomes"

    result = {outcome: 0 for outcome in outcome_names}

    for item in list_outcomes:
        result[item] = result.get(item, 0) + 1

    return result


# show result of a test in specific format
def show_result(
    title,
    selected_outcome,
    total_experiments,
    experimental_probability,
    theoretical_probability,
    difference,
    mean,
    median,
    variance,
    standard_deviation,
):
    "show result of a test in specific format"

    # show
    print(f"========== {title} ==========" + "\n")

    print(f"{'selected_outcome':<25}: {selected_outcome:>10}" + "\n")

    print(f"{'total_experiments':<25}: {total_experiments:>10}" + "\n")

    print(
        f"{'experimental_probability':<25}: {experimental_probability:>10.2f}%" + "\n"
    )

    print(f"{'theoretical_probability':<25}: {theoretical_probability:>10.2f}%" + "\n")

    print(f"{'difference':<25}: {difference:>10.2f}%" + "\n")

    print(f"----- Statistical Measures -----" + "\n")

    print(f"{'mean':<25}: {mean:>10.2f}" + "\n")

    print(f"{'median':<25}: {median:>10.2f}" + "\n")

    print(f"{'variance':<25}: {variance:>10.2f}" + "\n")

    print(f"{'standard_deviation':<25}: {standard_deviation:>10.2f}" + "\n")
