def solve(A, B):
   A = A[:]
   B = B[:]
   N = len(A)
   M = len(B)
   start = min(range(M), key=lambda j:B[j])
   B = B[start:] + B[:start]

   cands = []
   for try_ in 0, 1:
      last = -M
      res = A[:]
      for i in range(N-M+1):
         if not (last + M <= i):
            res[i] = B[i - last]


         if res[i] < B[0]:
            continue

         if res[i] > B[0]:
            last = i
            res[i] = B[0]
            continue

         if res[i] == B[0]:
            if try_:
               last = i
               res[i] = B[0]
               continue
            else:
               pass
      for i in range(N-M+1, N):
         if last + M <= i:
            continue
         else:
            res[i] = B[i - last]
      cands.append(res)
   return min(cands)


T = int(input())
for _ in range(T):
   N, M = map(int, input().split())
   A = list(map(int, input().split()))
   B = list(map(int, input().split()))
   print(*solve(A, B))