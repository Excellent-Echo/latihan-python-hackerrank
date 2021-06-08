import math
import os
import random
import re
import sys


def migratoryBirds(arr):
    highest_count = 0
    highest_bird = 0
    for i in range (1, 6):
        count = len([bird for bird in arr if bird == i])
        if highest_count < count:
            highest_count = count
            highest_bird = i
    return highest_bird


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    arr_count = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    result = migratoryBirds(arr)
    fptr.write(str(result) + '\n')
    fptr.close()
