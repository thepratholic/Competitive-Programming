from sys import stdin
from collections import *

input = stdin.readline

def solve():
    n = int(input())

    if n <= 1399:
        print("Division 4")

    if n >= 1400 and n <= 1599:
        print("Division 3")


    if n >= 1600 and n <= 1899:
        print("Division 2")

    if n >= 1900:
        print("Division 1")

t = int(input())
for _ in range(t):
    solve()