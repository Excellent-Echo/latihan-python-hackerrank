import math
import os
import random
import re
import sys

def sockMerchant(n, ar):
    unique_color = set(ar)
    amount_color = {color: 0 for color in unique_color}
    for color in ar:
        amount_color[color] += 1
    amount_pairs = 0
    for color in unique_color:
        amount_pairs += amount_color[color]//2
    return amount_pairs

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    n = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = sockMerchant(n, ar)
    fptr.write(str(result) + '\n')
    fptr.close()
