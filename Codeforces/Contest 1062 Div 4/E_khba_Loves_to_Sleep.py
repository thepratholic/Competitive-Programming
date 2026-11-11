import sys
input = sys.stdin.readline

def solve():
    n, k, X = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()

    def check(mid):
        if mid == 0:
            return True

        bad = []
        for val in a:
            l = max(0, val - mid + 1)
            r = min(X, val + mid - 1)
            if l <= r:
                bad.append((l, r))

        if not bad:
            return True

        bad.sort()
        merged = []
        cl, cr = bad[0]
        for l, r in bad[1:]:
            if l <= cr + 1:
                cr = max(cr, r)
            else:
                merged.append((cl, cr))
                cl, cr = l, r
        merged.append((cl, cr))

        free = X + 1
        for l, r in merged:
            free -= (r - l + 1)

        return free >= k

    low, high = 0, X
    best = 0

    while low <= high:
        mid = (low + high) // 2
        if check(mid):
            best = mid
            low = mid + 1
        else:
            high = mid - 1

    # Step 3: actually place teleports
    bad = []
    for val in a:
        l = max(0, val - best + 1)
        r = min(X, val + best - 1)
        if l <= r:
            bad.append((l, r))

    bad.sort()
    merged = []
    if bad:
        cl, cr = bad[0]
        for l, r in bad[1:]:
            if l <= cr + 1:
                cr = max(cr, r)
            else:
                merged.append((cl, cr))
                cl, cr = l, r
        merged.append((cl, cr))

    ans = []
    pos = 0
    for l, r in merged:
        while pos < l and len(ans) < k:
            ans.append(pos)
            pos += 1
        pos = r + 1
        if len(ans) == k:
            break

    while len(ans) < k and pos <= X:
        ans.append(pos)
        pos += 1

    print(*ans)

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        solve()
