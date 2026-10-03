from subprocess import run
from msvcrt import getwch


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
        except ValueError:
            print("Please enter total repeat as a number ... \n")

    return total
