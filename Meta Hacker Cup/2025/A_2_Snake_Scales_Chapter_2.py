import sys
from collections import *

# ==========================================
# META HACKER CUP TEMPLATE
# ==========================================

INPUT_FILE = "snake_scales_chapter_2_input.txt"
OUTPUT_FILE = "output.txt"


def solve():
    n = int(input())
    a = list(map(int, input().split()))

    lo, hi = 0, 10**9
    ans = -1

    while lo <= hi:
        mid = (lo + hi) >> 1

        vis = [0] * n

        for i in range(n):
            if a[i] <= mid:
                vis[i] = 1

            elif (i > 0 and vis[i - 1] and abs(a[i] - a[i - 1]) <= mid):
                vis[i] = 1

        for i in range(n - 2, -1, -1):
            if (vis[i + 1] and abs(a[i] - a[i + 1]) <= mid):
                vis[i] = 1

        if all(vis):
            ans = mid
            hi = mid - 1
        else:
            lo = mid + 1

    return ans


# ==========================================
# MAIN
# ==========================================

if __name__ == "__main__":

    # Local testing
    if __debug__:
        try:
            fin = open(INPUT_FILE, "r")
            fout = open(OUTPUT_FILE, "w")

            input = fin.readline

            t = int(input())

            for case in range(1, t + 1):
                ans = solve()
                fout.write(f"Case #{case}: {ans}\n")

            fin.close()
            fout.close()

        except FileNotFoundError:
            # If input file is not found,
            # use normal stdin/stdout
            input = sys.stdin.readline

            t = int(input())

            for case in range(1, t + 1):
                ans = solve()
                print(f"Case #{case}: {ans}")