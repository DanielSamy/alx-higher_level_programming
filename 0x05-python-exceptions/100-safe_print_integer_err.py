#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    is_int = True
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        is_int = False
        return is_int
