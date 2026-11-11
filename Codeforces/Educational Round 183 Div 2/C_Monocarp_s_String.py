import sys
from collections import defaultdict as dd

def solve():
    n = int(input())
    s = input().strip()

    a, b = s.count('a'), s.count('b')
    if a == b:
        print(0)
        return
    if a == 0 or b == 0:
        print(-1)
        return

    d = a - b
    ans = float('inf')
    pref = 0
    mp = dd(list)
    mp[0].append(0)

    for j, ch in enumerate(s):
        pref += 1 if ch == 'a' else -1
        need = pref - d
        if need in mp:
            i = mp[need][-1]
            ans = min(ans, j - i + 1)
        mp[pref].append(j + 1)

    print(-1 if ans == float('inf') or ans == n else ans)

t = int(input())
for _ in range(t):
    solve()
