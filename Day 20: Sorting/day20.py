#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    a = map(int, raw_input().rstrip().split())
    swap = 0
    for i in range(n):
        for j in range(i, n):
            if a[i]>a[j]:
                a[i], a[j] = a[j], a[i]
                swap+=1
                
    print("Array is sorted in {:.0f} swaps.".format(swap))
    print("First Element: {:.0f}".format(a[0]))
    print("Last Element: {:.0f}".format(a[-1]))
