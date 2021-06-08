import math
import os
import random
import re
import sys


def angry_professor(k, a):
	on_time = 0
	for x in a:
		if x <= 0:
			on_time += 1

	return 'YES' if on_time < k else 'NO'


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	t = int(input().strip())
	for t_itr in range(t):
		first_multiple_input = input().rstrip().split()
		n = int(first_multiple_input[0])
		k = int(first_multiple_input[1])
		a = list(map(int, input().rstrip().split()))
		result = angry_professor(k, a)
		fptr.write(result + '\n')
	fptr.close()
