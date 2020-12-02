#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    sum = 0
    min = max = arr[0]
    for e in arr:
        if e < min:
            min = e
        if e > max:
            max = e
        sum += e
    print(str(sum - max) + " " + str(sum - min))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
