#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':

    n = int(input())

    print(*[i for i in range(1, n+1)], sep='')
