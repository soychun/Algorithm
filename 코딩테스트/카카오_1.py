#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'solution' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x
#  2. INTEGER y
#  3. INTEGER z
#

def solution(x, y, z):
    print(x, y, z)
    if abs(x - y) > z:
        return -1
    elif abs(x - y) == z:
        print(max(x, y))
        return max(x, y)
    elif x == y:
        if z == 1:
            return -1
        else:
            return x + int(z / 2)
    elif x < y:
        return int(y + (z - abs(y - x)) // 2)
    elif y < x:
        return int(x + (z - abs(y - x)) // 2)
        # print('abs',abs(x-y))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x = int(input().strip())

    y = int(input().strip())

    z = int(input().strip())

    result = solution(x, y, z)

    fptr.write(str(result) + '\n')

    fptr.close()
