import math
import os
import random
import re
import sys



def repeated_string(string, amount_char):
	pos = [i for i, x in enumerate(string) if x == 'a']
	res = len(pos) * (amount_char//len(string))
	leftovers = amount_char % len(string)
	res += len([x for x in pos if x < leftovers])
	return res


if __name__ == '__main__':
	fptr = open(os.environ['OUTPUT_PATH'], 'w')
	s = input()
	n = int(input().strip())
	result = repeated_string(s, n)
	fptr.write(str(result) + '\n')
	fptr.close()
