import sys
 
if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(6000)

def fact(x):
    if x == 0: 
        return 1
    return x * fact(x - 1)

def solve():
    n, k = map(int, input().split())

    n = min(n, 7)

    s = int(str(k) * fact(n))

    for i in range(1, 10, 2):
        if s % i == 0:
            print(i, end = ' ')
    print()


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()