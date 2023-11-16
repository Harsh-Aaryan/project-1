#!/usr/bin/python3
# -*- coding: utf-8 -*-


def collatz_verifier(l: list[int]) -> list[list[int]]:
    """Verify that every integer in l eventually results in 1.

    For each integer in l, create a list of every step until resulting in 1.
    l will only contain positive integers!

    :param l: List of integers to verify.
    :return: List containing a list of the path each integer in l took to get to 1.

    Usage illustrated via some simple doctests:
    >>> collatz_verifier([1])
    [[1]]

    >>> collatz_verifier([1, 2, 5])
    [[1], [2, 1], [5, 16, 8, 4, 2, 1]]
    """
    # To debug doctest test in pudb
    # Highlight the line of code below
    # Type 't' to jump 'to' it
    # Type 's' to 'step' deeper
    # Type 'n' to 'next' over
    # Type 'f' or 'r' to finish/return a function call and go back to caller

    # Your code goes here >>>>>
    pass

    # <<<<<


if __name__ == "__main__":
    # Execute doctests to protect main:
    import doctest

    doctest.testmod()

    # Run main:
    nums_to_verify = [
        int(v) for v in input().split(" ")
    ]  # input like '1 2 3 4' without quotes
    print(collatz_verifier(nums_to_verify))
