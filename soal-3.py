#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'migratoryBirds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def migratoryBirds(arr):
    # Write your code here
    type = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }

    for i in arr:
        if i == 1:
            type[1] += 1
        elif i == 2:
            type[2] += 1
        elif i == 3:
            type[3] += 1
        elif i == 4:
            type[4] += 1
        else:
            type[5] += 1

    max = 0
    answer = 0
    for key in type:
        if max < type[key]:
            max = type[key]
            answer = key

    return answer


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
