import sys
from itertools import permutations
input = sys.stdin.readline

def sorted_perms(s):
    return sorted(''.join(p) for p in permutations(s))

perm_12 = sorted_perms("12")
perm_123 = sorted_perms("123")
perm_1234 = sorted_perms("1234")

def solve():
    n, j, k = input().split()
    j = int(j) - 1
    k = int(k) - 1

    if n == "12":
        s1 = perm_12[j]
        s2 = perm_12[k]

    elif n == "123":
        s1 = perm_123[j]
        s2 = perm_123[k]

    else:
        s1 = perm_1234[j]
        s2 = perm_1234[k]

    a = 0
    b = 0
    used = [False] * len(n)

    for i in range(len(n)):
        if s1[i] == s2[i]:
            a += 1
            used[i] = True

    for i in range(len(n)):
        if s1[i] != s2[i]:
            for j in range(len(n)):
                if not used[j] and s1[i] == s2[j] and i != j:
                    b += 1
                    used[j] = True
                    break

    print(f"{a}A{b}B")

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
