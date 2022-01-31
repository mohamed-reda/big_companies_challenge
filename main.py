#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pointsBelong' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER x1
#  2. INTEGER y1
#  3. INTEGER x2
#  4. INTEGER y2
#  5. INTEGER x3
#  6. INTEGER y3
#  7. INTEGER xp
#  8. INTEGER yp
#  9. INTEGER xq
#  10. INTEGER yq
#
def area(x1, y1, x2, y2, x3, y3):
    return abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0)


def result(p, q):
    if p and q:
        print(3)
    elif p and not q:
        print(1)
    elif not p and q:
        print(2)
    else:
        print(4)


def pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq):
    a = (x1 * (y2 - y3) +
         x2 * (y3 - y1) +
         x3 * (y1 - y2))
    if a == 0:
        print(0)
    else:
        the_true_of_p_and_q = [False, False]
        index = 0
        for i in [[xp, yp], [xq, yq]]:
            a = area(x1, y1, x2, y2, x3, y3)
            a1 = area(i[0], i[1], x2, y2, x3, y3)
            a2 = area(x1, y1, i[0], i[1], x3, y3)
            a3 = area(x1, y1, x2, y2, i[0], i[1])
            the_true_of_p_and_q[index] = (a == a1 + a2 + a3)
            index += 1      
        result(the_true_of_p_and_q[0], the_true_of_p_and_q[1])
        """
        I don't know why I'm getting None output with any test case but here what happens       with the same code at my labtop using Pycharm:
        test case 1: 
input:
0
0
2
0
4
0
2
0
4
0
output:
0

        test case 2:
input:
3    
1 
7    
1 
5    
5 
3    
1 
0    
0
output:
1
        """


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    x1 = int(input().strip())

    y1 = int(input().strip())

    x2 = int(input().strip())

    y2 = int(input().strip())

    x3 = int(input().strip())

    y3 = int(input().strip())

    xp = int(input().strip())

    yp = int(input().strip())

    xq = int(input().strip())

    yq = int(input().strip())

    result = pointsBelong(x1, y1, x2, y2, x3, y3, xp, yp, xq, yq)

"""
input:
0
0
2
0
4
0
2
0
4
0
output:
0

test case 2:
input:
3    
1 
7    
1 
5    
5 
3    
1 
0    
0
output:
1
"""
