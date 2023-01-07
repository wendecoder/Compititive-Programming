#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    l = len(grades)
    for i in range(0, l):
        k = (grades[i] / 5)
        l = round(k)
        j = l * 5
        if j < grades[i]:
            j = j + 5
        if grades[i] < 38:
            pass
        elif j - grades[i] < 3:
            grades[i] = j
        elif j - grades[i] >= 3:
            pass
        
    return grades
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
