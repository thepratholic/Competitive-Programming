from collections import deque


def solve():
    n = int(input())

    graph = [[] for _ in range(n + 1)]

    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    def bfs(start):
        dist = [-1] * (n + 1)

        q = deque([start])
        dist[start] = 0
        far_node = start

        while q:
            u = q.popleft()

            for v in graph[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    far_node = v
                    q.append(v)

        return far_node, dist

    A, _ = bfs(1)
    B, dist_a = bfs(A)
    _, dist_b = bfs(B)

    diameter = dist_a[B]
    k = diameter // 2

    C1 = -1
    C2 = -1

    for i in range(1, n + 1):
        if dist_a[i] + dist_b[i] == diameter:
            if dist_a[i] == k:
                C1 = i
            elif dist_a[i] == k + 1:
                C2 = i

    def dfs(start, parent, k, values):
        def dfs_inner(u, p, depth):
            max_depth = depth
            branches = 0

            for v in graph[u]:
                if v == p:
                    continue

                child_max = dfs_inner(v, u, depth + 1)

                max_depth = max(max_depth, child_max)

                if child_max == k:
                    branches += 1

            if branches >= 2:
                values.add(depth)

            return max_depth

        dfs_inner(start, parent, 0)

    S1 = {k}
    S2 = {k}

    dfs(C1, C2, k, S1)
    dfs(C2, C1, k, S2)

    ans = set()

    for x in S1:
        for y in S2:
            ans.add(x + y + 1)

    ans = sorted(ans)

    print(len(ans), *ans)


t = int(input())

for _ in range(t):
    solve()