#!/bin/python

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(raw_input().strip())
    arr = map(int, raw_input().rstrip().split())
    arr1 = arr.reverse()
    list1=list(arr)
    print(' '.join(map(str, list1))) 
