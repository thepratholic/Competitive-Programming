import sys
import heapq
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    casinos = [tuple(map(int, input().split())) for __ in range(n)]
    casinos.sort(key=lambda x: x[0])

    max_coins = k
    ptr = 0
    heap = []

    visited = [False] * n
    coins = k


    while True:
        while ptr < n and casinos[ptr][0] <= coins:
            li, ri, reali = casinos[ptr]
            heapq.heappush(heap, (-reali, ri, ptr))
            ptr += 1

        changed = False
        while heap:
            neg_reali, ri, idx = heapq.heappop(heap)
            if visited[idx]:
                continue
            if coins <= ri:
                visited[idx] = True
                coins = -neg_reali
                max_coins = max(max_coins, coins)
                changed = True
                break

        if not changed:
            break

    print(max_coins)
