import logging
import subprocess  # nosec
from typing import Optional

logger = logging.getLogger(__name__)


def run_command(
    command: str, exit_on_error: bool = True, return_stdout: bool = False, cwd: Optional[str] = None
) -> str:
    """
    Run a command in the shell.

    :param command: The command to run.
    :param exit_on_error: Whether to exit the program if the command fails.
    :param return_stdout: Whether to return the stdout of the command.
    :param cwd: The current working directory to run the command in.
    :return: The result of the command stdout or an empty string in case return_stdout is False.
    """
    logger.debug(f"Running command: {command}")

    process = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        shell=True,
        cwd=cwd,
    )  # nosec
    if process.stdout != "\n":
        logger.debug(process.stdout.rstrip("\n"))
    stdout = process.stdout if return_stdout else ""

    if process.returncode != 0 and exit_on_error:
        if return_stdout:
            logger.error(stdout)
        exit(1)

    return stdout


def escape_quotes(value: str) -> str:
    """
    Escape quotes ' and " in a string.

    :param value: The string to escape.
    :return: The string with escaped quotes
    """
    return value.replace("'", "\\'").replace('"', '\\"')


def ensure_alphanumeric_start(input_string: str) -> str:
    """
    Ensures that the string starts with an alphanumeric character.
    If not, recursively remove the first character and check again.
    If the string is empty, return "default".

    :param input_string: The string to be checked.
    :return: A string which starts with an alphanumeric character, or "default" if the string is empty.
    """
    if not input_string:
        return "default"

    if input_string[0].isalnum():
        return input_string
    else:
        return ensure_alphanumeric_start(input_string[1:])
