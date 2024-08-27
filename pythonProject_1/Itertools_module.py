import math
import os
import random
import re
import sys
import itertools


def performIterator(tuplevalues):
    lst_main = []

    # Part 1
    lst_alt = []
    cycle = itertools.cycle(tuplevalues[0])
    for _ in range(4):
        lst_alt.append(cycle.__next__())
    lst_main.append(tuple(lst_alt))

    # Part 2
    lst_alt = []
    repeater = itertools.repeat(tuplevalues[1][0], len(tuplevalues[1]))
    for val in repeater:
        lst_alt.append(val)
    lst_main.append(tuple(lst_alt))

    # Part 3
    lst_alt = []
    accumulate = itertools.accumulate(tuplevalues[2])
    for val in accumulate:
        lst_alt.append(val)
    lst_main.append(tuple(lst_alt))

    # Part 4
    lst_alt = []
    for n in tuplevalues:
        chained = itertools.chain(n)
        for val in chained:
            lst_alt.append(val)
    lst_main.append(tuple(lst_alt))

    # Part 5
    num = lst_alt
    lst_alt = []
    filetred = itertools.filterfalse(lambda x: x % 2 == 0, num)
    for val in filetred:
        lst_alt.append(val)
    lst_main.append(tuple(lst_alt))

    return tuple(lst_main)


if __name__ == '__main__':

    length = int(input().strip())

    qw1 = []
    for i in range(4):
        qw2 = []
        for _ in range(length):
            qw2_item = int(input().strip())
            qw2.append(qw2_item)
        qw1.append(tuple(qw2))
    tupb = tuple(qw1)

    q = performIterator(tupb)
    print(q)
