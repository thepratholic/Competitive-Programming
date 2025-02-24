def solve():
    n, a, b, c = map(int, input().split())

    cycle_sum = a + b + c
    full_cycles = n // cycle_sum
    remaining = n % cycle_sum

    if remaining == 0:
        print(full_cycles * 3)
        return

    day = full_cycles * 3 + 1

    for step in [a, b, c]:
        if remaining <= 0:
            break
        remaining -= step
        day += 1

    print(day - 1)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
