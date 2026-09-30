from subprocess import run


# run a commant in terminal
def run_command(command: str) -> None:
    if command:
        run(f"{command}", shell=True)
