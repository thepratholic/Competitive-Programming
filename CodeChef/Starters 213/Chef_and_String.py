import sys
input = sys.stdin.readline

def solve():
    n,k = map(int, input().split())
    s = input().strip()
    fixed = [c for c in s if c != 'I']
    if not fixed:
        print(n * k - 1)
        return
    cnt = 0
    for i in range(len(fixed)-1):
        if fixed[i] != fixed[i+1]:
            cnt += 1
    bd = 1 if fixed[0] != fixed[-1] else 0
    total_pairs = n * k - 1
    min_trans = cnt * k + bd * (k - 1)
    print(total_pairs - min_trans)

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()
