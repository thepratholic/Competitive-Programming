def solve():
    n = int(input())
    a = list(map(int, input().split()))

    longest = 0
    curr = 0
    for i in range(n):
        if a[i] == 0:
            curr += 1
            longest = max(longest, curr)
        else:
            curr = 0

    print(longest)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()