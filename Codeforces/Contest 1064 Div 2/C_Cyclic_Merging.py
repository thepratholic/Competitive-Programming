# import sys
# from collections import defaultdict, Counter, deque
# from heapq import heappush, heappop, heapify
# from math import gcd, ceil, floor, sqrt
# from functools import lru_cache, reduce
# from bisect import bisect, bisect_left, bisect_right
# from itertools import accumulate, permutations, groupby
# input = sys.stdin.readline

# def solve():
#     n = int(input())
#     a = list(map(int, input().split()))

#     ans = 0

#     q = deque(a)

#     while len(q) > 2:
#         f = q.popleft()
#         s = q.popleft()
#         l = q.pop()

#         if max(f, l) <= max(f, s):

#             if f == l:
#                 q.append(l)
#                 q.appendleft(s)
#                 ans += max(f, l)
#             elif f > l:
#                 q.appendleft(s)
#                 q.appendleft(f)
#                 ans += max(f, l)
#             else:
#                 q.append(l)
#                 q.appendleft(s)
#                 ans += max(f, l)

#         else:
#             if f == s:
#                 q.appendleft(s)
#                 q.append(l)
#                 ans += max(f, s)

#             elif f > s:
#                 q.appendleft(f)
#                 q.append(l)
#                 ans += max(f, s)
#             else:
#                 q.appendleft(s)
#                 q.append(l)
#                 ans += max(f, s)

#     ans += max(q[0], q[1])
#     print(ans)

# if __name__ == '__main__':
#     t = int(input())
#     for _ in range(t):
#         solve()



import sys
from collections import defaultdict, Counter, deque
from heapq import heappush, heappop, heapify
from math import gcd, ceil, floor, sqrt
from functools import lru_cache, reduce
from bisect import bisect, bisect_left, bisect_right
from itertools import accumulate, permutations, groupby
input = sys.stdin.readline

def solve():
    n = int(input())
    a = list(map(int, input().split()))
    edges = [max(a[i], a[(i+1) % n]) for i in range(n)]
    print(sum(edges) - max(edges))

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
