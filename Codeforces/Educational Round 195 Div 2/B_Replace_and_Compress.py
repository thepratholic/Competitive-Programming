from sys import stdin
from collections import *

input = stdin.readline

def solve():
    # n = int(input())
    # a = list(map(int, input().split()))
    s = input().strip()
    n = len(s)

    st = set()


    for i in range(1, n - 1):
        if s[i - 1] == '0' and s[i] == '0' and s[i + 1] == '0':
            st.add(2)

        if s[i - 1] == '1' and s[i] == '1' and s[i + 1] == '1':
            st.add(2)

        if s[i - 1] == '0' and s[i] == '1' and s[i + 1] == '0':
            st.add(-2)

        if s[i - 1] == '1' and s[i] == '0' and s[i + 1] == '1':
            st.add(-2)

    print(len(st) + 1)
    

t = int(input())
for _ in range(t):
    solve()