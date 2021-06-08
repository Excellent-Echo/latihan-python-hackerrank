#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#


def repeatedString(s, n):
    # Write your code here
    x = int(n / len(s))
    mod = n % len(s)
    # print(x, mod)

    front_str = s[:mod]
    # print(front_str)
    back_str = s[mod:]
    # print(back_str)
    total_1 = front_str.count("a")*(x+1)
    total_2 = back_str.count("a")*x
    return total_1 + total_2


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
