def solve():
    A1, B1, A2, B2 = map(int, input().split())
    
    val1 = 5 * A1 + B1
    val2 = 5 * A2 + B2
    
    if val1 >= val2 and (val1 - val2) % 6 == 0:
        print("Yes")
    else:
        print("No")

T = int(input())
for _ in range(T):
    solve()