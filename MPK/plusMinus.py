#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    # Write your code here
    p = n = z = 0
    l = len(arr)
    for x in arr:
        if x > 0:
            p += 1
        elif x < 0:
            n += 1
        else:
            z += 1
    print("{0:.6f}".format(p/l))
    print("{0:.6f}".format(n/l))
    print("{0:.6f}".format(z/l))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
