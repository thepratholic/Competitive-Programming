def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    idx = 1
    ans = []
    for _ in range(t):
        n = int(data[idx]); k = int(data[idx+1]); idx += 2
        A = list(map(int, data[idx:idx+n])); idx += n
        B = list(map(int, data[idx:idx+n])); idx += n
        s_min = 0
        r_min = None
        for a, b in zip(A, B):
            diff = (b - a) % 9
            if diff == 0:
                m = 0
                r = 9
            else:
                m = min(diff, 9 - diff)
                r = abs(9 - 2*m)
            s_min += m
            if r_min is None or r < r_min:
                r_min = r
        if s_min > k:
            ans.append("NO")
        else:
            if s_min % 2 == k % 2:
                base = s_min
            else:
                base = s_min + r_min
            ans.append("YES" if base <= k else "NO")
    sys.stdout.write("\n".join(ans))

if __name__ == '__main__':
    solve()
