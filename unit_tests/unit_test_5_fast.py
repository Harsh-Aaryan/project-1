#!/usr/bin/python3
# -*- coding: utf-8 -*-

import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Your code tests start here:
# To debug in pudb3
# Highlight the line of code below below
# Type 't' to jump 'to' it
# Type 's' to 'step' deeper
# Type 'n' to 'next' over
# Type 'f' or 'r' to finish/return a function call and go back to caller
from collatz_verifier import collatz_verifier
from time import time


def oracle(OOO0OOOO0000000O0: list[int]) -> list[list[int]]:
    """Decide to have a look around, did ya? Well, good luck!"""
    O0O000OO0OOO0O00O = {}
    for OOO0OOO00OO000OO0 in OOO0OOOO0000000O0:
        O0OOO0OO0O0OO00OO = [OOO0OOO00OO000OO0]
        while O0OOO0OO0O0OO00OO[-1] != 1:
            if O0OOO0OO0O0OO00OO[-1] in O0O000OO0OOO0O00O:
                O0OOO0OO0O0OO00OO += O0O000OO0OOO0O00O[O0OOO0OO0O0OO00OO[-1]][1:]
                break
            if O0OOO0OO0O0OO00OO[-1] % 2:
                O0OOO0OO0O0OO00OO.append(3 * O0OOO0OO0O0OO00OO[-1] + 1)
            else:
                O0OOO0OO0O0OO00OO.append(O0OOO0OO0O0OO00OO[-1] // 2)
        for O00O000O000O00OOO, O0000OOOO0O0O0O00 in enumerate(O0OOO0OO0O0OO00OO):
            if O0000OOOO0O0O0O00 not in O0O000OO0OOO0O00O:
                O0O000OO0OOO0O00O[O0000OOOO0O0O0O00] = O0OOO0OO0O0OO00OO[
                    O00O000O000O00OOO:
                ]
            else:
                break
    return [
        O0O000OO0OOO0O00O[O0O0000OO0O0OOOO0] for O0O0000OO0O0OOOO0 in OOO0OOOO0000000O0
    ]


big_list = list(range(1, 100001))

start = time()
oracle_results = oracle(big_list)
oracle_time = time() - start + 0.2  # A little buffer time

start = time()
student_results = collatz_verifier(big_list)
student_time = time() - start

assert student_results == oracle_results
assert student_time <= oracle_time
