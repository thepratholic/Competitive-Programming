def solve():
    import sys
    data = sys.stdin.read().split()
    t = int(data[0])
    pos = 1
    out_lines = []
    for _ in range(t):
        N = int(data[pos]); pos += 1
        arr = list(map(int, data[pos:pos+N])); pos += N
        
        if N == 1:
            out_lines.append(str(arr[0]))
            continue
        
        total_ops = (N - 1) // 2
        best = 0
        for i in range(N):
            left_cost = (i + 1) // 2
            right_cost = (N - i) // 2
            cost = min(left_cost, right_cost)
            boost = total_ops - cost
            candidate = arr[i] + boost
            if candidate > best:
                best = candidate
        out_lines.append(str(best))
    sys.stdout.write("\n".join(out_lines))

if __name__ == "__main__":
    solve()
