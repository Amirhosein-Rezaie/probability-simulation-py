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
