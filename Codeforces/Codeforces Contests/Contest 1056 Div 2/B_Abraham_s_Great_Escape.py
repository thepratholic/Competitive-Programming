import sys

def solve():
    input = sys.stdin.read
    data = input().split()
    
    if not data:
        return

    t = int(data[0])
    ptr = 1
    res = []

    for _ in range(t):
        if ptr + 1 > len(data):
            break
        
        n = int(data[ptr])
        k = int(data[ptr+1])
        ptr += 2

        N = n * n
        
        if k == N - 1 and n > 1:
            res.append("NO")
            continue

        res.append("YES")
        
        g = [[''] * n for _ in range(n)]

        
        for i in range(k):
            r, c = i // n, i % n
            g[r][c] = 'U'

        M = N - k

        if M > 0:
            r_c1, c_c1 = n - 1, n - 1
            r_c2, c_c2 = n - 1, n - 2

            idx_c1 = r_c1 * n + c_c1
            idx_c2 = r_c2 * n + c_c2

            for i in range(k, N):
                r, c = i // n, i % n
                
                if (r, c) == (r_c1, c_c1):
                    g[r][c] = 'L'
                elif (r, c) == (r_c2, c_c2):
                    g[r][c] = 'R'
                else:
                    if r < r_c1:
                        g[r][c] = 'D'
                    elif c < c_c2:
                        g[r][c] = 'R'


        for r in g:
            res.append("".join(r))

    sys.stdout.write("\n".join(res) + "\n")

if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    solve()