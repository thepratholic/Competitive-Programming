from collections import Counter
import sys

input = sys.stdin.readline


def solve():
  n = int(input())
  a = list(map(int, input().split()))

  tot = [0] * 101
  for x in a:
    tot[x] += 1

  res = []
  cur = [0] * 101
  mf = 0
  cm = -1

  for _ in range(n):
    best_e = -1
    best_m = -1

    for e in range(1, 101):
      if tot[e] > 0:
        f_e = cur[e] + 1
        if f_e > mf:
          cur_mf, cur_cm = f_e, e
        elif f_e == mf:
          cur_mf, cur_cm = mf, max(cm, e)
        else:
          cur_mf, cur_cm = mf, cm

        if cur_cm > best_m:
          best_m = cur_cm
          best_e = e
        elif cur_cm == best_m:
          if e > best_e:
            best_e = e

    res.append(best_e)
    cur[best_e] += 1
    tot[best_e] -= 1

    if cur[best_e] > mf:
      mf = cur[best_e]
      cm = best_e
    elif cur[best_e] == mf:
      cm = max(cm, best_e)

  print(*res)


t = int(input())
for _ in range(t):
  solve()