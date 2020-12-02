#!/bin/python3

import os
import sys
import re

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    elements = s.split(':')
    am_pm = elements[2][2:4]
    elements[2] = elements[2][0:2]
    hour = int(elements[0])

    if elements[0] == '12' and am_pm == 'AM':
        elements[0] = '00'
    if hour != 12 and am_pm == 'PM':
        hour += 12
        elements[0] = str(hour)

    return elements[0] + ':' + elements[1] + ':' + elements[2]

if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')
    #
    # s = input()
    s='12:01:01AM'

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
