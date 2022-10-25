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
    x = arr.pop()
    arr.append(x)

    while (arr[n-2]!=x):
        if(arr[n-2]>x):
            arr[n-1]=arr[n-2]
            print(" ".join(map(str,arr)))
        else:
            arr[n-1]=x
            print(" ".join(map(str,arr)))
            break
        n=n-1  

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
