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


def oracle(O000OOO0O0OOO00O0):
    """Decide to have a look around, did ya? Well, good luck!"""
    OOO00O0OOOOO0OO00 = []
    for OOOOOOO00OOOOOO00 in O000OOO0O0OOO00O0:
        OO0000OOO000O0O0O = [OOOOOOO00OOOOOO00]
        while OO0000OOO000O0O0O[-1] != 1:
            if OO0000OOO000O0O0O[-1] % 2:
                OO0000OOO000O0O0O.append(3 * OO0000OOO000O0O0O[-1] + 1)
            else:
                OO0000OOO000O0O0O.append(OO0000OOO000O0O0O[-1] // 2)
        OOO00O0OOOOO0OO00.append(OO0000OOO000O0O0O)
    return OOO00O0OOOOO0OO00


big_list = list(range(1, 100001))

start = time()
oracle_results = oracle(big_list)
oracle_time = time() - start + 0.5  # A little buffer time

start = time()
student_results = collatz_verifier(big_list)
student_time = time() - start

assert student_results == oracle_results
assert student_time <= oracle_time
