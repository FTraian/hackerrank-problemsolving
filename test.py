#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the angryProfessor function below.
def angryProfessor(k, a):
    counter = 0;
    for e in a:
        if e > 0:
            counter += 1
        if counter == k:
            return "YES"
    return "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # t = int(input())

    result = angryProfessor(3, [-1, -3, 4, 2])
    # for t_itr in range(t):
    #     nk = input().split()
    #
    #     n = int(nk[0])
    #
    #     k = int(nk[1])
    #
    #     a = list(map(int, input().rstrip().split()))
    #
    #
    #     fptr.write(result + '\n')

    # fptr.close()
