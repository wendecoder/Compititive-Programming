#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#

def countSwaps(a):
    # Write your code here
    n = len(a)
    c = 0
    for i in range(n):
        for j in range(n - 1):
            if(a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp
                c = c + 1
    print("Array is sorted in {} swaps.".format(c))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[n - 1]))
    return 
    
                

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
