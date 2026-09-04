import sys
from math import *
from collections import *
from itertools import *
from functools import *
from heapq import *
from bisect import *


# ==========================================
# META HACKER CUP TEMPLATE
# ==========================================

INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def solve():
    # Read input for ONE test case
    n = int(input())
    a = list(map(int, input().split()))

    # Your logic
    ans = 0

    return ans


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    # Read from file
    with open(INPUT_FILE, "r") as fin, \
         open(OUTPUT_FILE, "w") as fout:

        input = fin.readline

        T = int(input())

        for tc in range(1, T + 1):
            ans = solve()
            fout.write(f"Case #{tc}: {ans}\n")