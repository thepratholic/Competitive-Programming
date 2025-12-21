import sys
input = sys.stdin.readline

def solve():
    n, k = map(int, input().split())

    if k == 1:
        print(n)
        return

    tight = k
    ans = [0] * k
    idx = n.bit_length() - 1

    for i in range(idx, -1, -1):
        if (n >> i) & 1:
            leave = -1
            if tight > 0 and k % 2 == 0:
                leave = tight - 1
                tight -= 1
            if k % 2 == 0 and leave == -1:
                leave = 0

            for j in range(k):
                if j != leave:
                    ans[j] |= (1 << i)
        else:
            rem = k - tight
            up = rem - (rem % 2)
            for j in range(k - 1, k - 1 - up, -1):
                ans[j] |= (1 << i)

    print(*ans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
