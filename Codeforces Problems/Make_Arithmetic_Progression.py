t = int(input())  # Number of test cases
for _ in range(t):
    x, y, z = map(int, input().split())
    
    # Check if 2 * y == x + z (i.e., the condition for arithmetic progression)
    if 2 * y == x + z:
        print(0)  # Already an AP, no operations needed
    else:
        print(1)