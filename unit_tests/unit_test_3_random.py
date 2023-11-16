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
import random


def oracle (O0000OOOO00O000OO :list [int ])->list [list [int ]]:#line:1
    """Decide to have a look around, did ya? Well, good luck!"""#line:2
    O00O00O0O0O0O0O00 =[]#line:3
    for OOOOOOOO0O000O000 in O0000OOOO00O000OO :#line:4
        O0O0O0OO0OOO0OOO0 =[OOOOOOOO0O000O000 ]#line:5
        while O0O0O0OO0OOO0OOO0 [-1 ]!=1 :#line:7
            if O0O0O0OO0OOO0OOO0 [-1 ]%2 :#line:8
                O0O0O0OO0OOO0OOO0 .append (3 *O0O0O0OO0OOO0OOO0 [-1 ]+1 )#line:9
            else :#line:10
                O0O0O0OO0OOO0OOO0 .append (O0O0O0OO0OOO0OOO0 [-1 ]//2 )#line:11
        O00O00O0O0O0O0O00 .append (O0O0O0OO0OOO0OOO0 )#line:13
    return O00O00O0O0O0O0O00


for _ in range(10):
    num = random.randint(1, 100001)
    result = oracle([num])
    assert collatz_verifier([num]) == result
