#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input())

    print(*[pow(i, 2) for i in range(0, n)], sep='\n')
