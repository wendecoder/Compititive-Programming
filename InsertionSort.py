#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    # Write your code here
    for i in range(1, n):
        j = i
        temp = arr[i]
        while(j > 0):
            if(arr[j] < arr[j - 1]):
                temp2 = arr[j - 1]
                arr[j] = temp2
                for l in range(n):
                    print(arr[l], end=" ")
                print()
                arr[j - 1] = temp
            j = j - 1
        if(i == n - 1):
            for k in range(n):
                print(arr[k], end=" ")
            print()
            
        
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
