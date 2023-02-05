"""
A command-line interface for calculating the harmonic mean of user-provided numbers.
"""

import sys
from imppkg.harmonic_mean import harmonic_mean
from termcolor import colored


def main() -> None:
    arg_list_command_line = sys.argv[1:]
    nums = _parse_nums(arg_list_command_line)
    harmonic_mean_ = _calculate_results(nums)
    harmonic_mean_colored = _format_output(harmonic_mean_)
    print(harmonic_mean_colored)


def _parse_nums(arg_list_command_line: list[str]) -> list[float]:
    nums: list[float] = [float(arg) for arg in arg_list_command_line]
    return nums


def _calculate_results(nums: list[float]) -> float:
    harmonic_mean_: float = harmonic_mean(nums)
    return harmonic_mean_


def _format_output(value: float) -> str:
    value_formatted: str = colored(str(value), "red", "on_cyan", attrs=["bold"])
    return value_formatted
