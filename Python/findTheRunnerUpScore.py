#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    n = int(input())
    arr = map(int, input().split())

    a = sorted(list(set(arr)))

    if(len(a) == 1):
        print(a[0])
    else:
        print(a[-2])
