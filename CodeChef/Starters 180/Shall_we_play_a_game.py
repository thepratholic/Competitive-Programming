MOD = 998244353

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    t = int(input_data[0])
    results = []
    index = 1
    for _ in range(t):
        N = int(input_data[index])
        index += 1
        if N % 2 == 1:
            ans = pow(2, N-1, MOD)
        else:
            ans = (3 * pow(2, N-2, MOD)) % MOD
        results.append(str(ans))
    sys.stdout.write("\n".join(results))

if __name__ == "__main__":
    solve()
