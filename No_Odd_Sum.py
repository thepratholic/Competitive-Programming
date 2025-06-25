def solve():
    N = int(input())
    A = list(map(int, input().split()))

    count_1 = 0
    count_2 = 0

    for x in A:
        if x == 1:
            count_1 += 1
        else:
            count_2 += 1

    if count_1 == 0 or count_2 == 0:
        print(0)
    else:
        ops_to_all_ones = count_2

        if count_1 % 2 == 0:
            ops_to_all_twos = count_1 // 2
            print(min(ops_to_all_ones, ops_to_all_twos))
        else:
            print(ops_to_all_ones)

T = int(input())
for _ in range(T):
    solve()