def can_be_sorted(n, a, b):
    b = b[0]  # b is always a single element

    # Generate two arrays: one keeping original a[i], one transforming
    a_transformed = [b - x for x in a]
    
    # Check if we can form a sorted array by selecting best option at each index
    prev_min = min(a[0], a_transformed[0])
    prev_max = max(a[0], a_transformed[0])

    possible = True
    for i in range(1, n):
        cur_min = min(a[i], a_transformed[i])
        cur_max = max(a[i], a_transformed[i])

        if cur_min >= prev_min and cur_max >= prev_max:
            prev_min, prev_max = cur_min, cur_max  # Both are valid, pick the min
        elif cur_min >= prev_max:  
            prev_min, prev_max = cur_min, cur_min  # Only `cur_min` is valid
        else:
            possible = False
            break

    return possible

# Input handling
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print("YES" if can_be_sorted(n, a, b) else "NO")
