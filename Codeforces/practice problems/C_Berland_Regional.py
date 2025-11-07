import sys
from collections import defaultdict
input = sys.stdin.readline

def solve():
    n = int(input())
    u = list(map(int, input().split()))
    s = list(map(int, input().split()))

    groups = defaultdict(list)
    for i in range(n):
        groups[u[i] - 1].append(s[i])

    ans = [0] * n

    for skills in groups.values():
        skills.sort(reverse=True)
        for i in range(1, len(skills)):
            skills[i] += skills[i - 1]

        m = len(skills)
        for k in range(1, m + 1):
            full = m // k
            if full > 0:
                used = full * k
                ans[k - 1] += skills[used - 1]

    print(*ans)

t = int(input())
for _ in range(t):
    solve()