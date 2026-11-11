def solve():

    n = int(input())
    a = list(map(int, input().split()))

    sum_even, sum_odd = 0, 0

    for i in range(n):
        if i % 2 == 0:
            sum_even += a[i]
        else:
            sum_odd += a[i]

    odd_place, even_place = n // 2, (n + 1) // 2

    if (sum_odd % odd_place == 0 and sum_even % even_place == 0 and sum_odd // odd_place == sum_even // even_place):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()