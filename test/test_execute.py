import sys

sys.path.append("../")

from main import execute


def test_execute() -> None:
    command = "python sample_function.py --a 1 --b 2"
    error_message = execute(command)
    assert error_message == ""

    command = "python sample_function.py --a 1.1 --b 2"
    error_message = execute(command)
    assert error_message != ""
