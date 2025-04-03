def solve():
    import sys
    input = sys.stdin.readline
    t = int(input())
    res = []
    for _ in range(t):
        n = int(input())
        p = list(map(int, input().split()))
        d = list(map(int, input().split()))
        cycle_id = [-1] * n
        cycle_size = []
        cur_id = 0
        vis = [False] * n
        for i in range(n):
            if not vis[i]:
                cur = i
                cnt = 0
                while not vis[cur]:
                    vis[cur] = True
                    cycle_id[cur] = cur_id
                    cnt += 1
                    cur = p[cur] - 1
                cycle_size.append(cnt)
                cur_id += 1
        intact = [True] * len(cycle_size)
        tot = n
        ans = []
        for pos in d:
            pos -= 1
            cid = cycle_id[pos]
            if intact[cid]:
                tot -= cycle_size[cid]
                intact[cid] = False
            ans.append(str(n - tot))
        res.append(" ".join(ans))
    sys.stdout.write("\n".join(res))


if __name__ == '__main__':
    solve()
