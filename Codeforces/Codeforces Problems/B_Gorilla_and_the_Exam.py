from collections import Counter

def solve():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    freq = sorted(Counter(a).values())
    ans = len(freq)

    for count in freq:
        if k >= count:
            k -= count
            ans -= 1
        else:
            break

    print(max(1, ans))

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
