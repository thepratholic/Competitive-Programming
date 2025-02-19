def solve_restaurant_name(N, A):
    if N == 1 and A == 'z':
        return "-1"
        
    mid = (N-1) // 2
    result = list(A)
    
    for i in range(mid + 1):
        orig_char = result[i]
        
        found = False
        for c in range(ord('a'), ord('z') + 1):
            result[i] = chr(c)
            temp = ''.join(result)

            if temp > A and temp[::-1] > A:
                found = True
                break

        if not found:
            result[i] = orig_char
            result[N-1-i] = orig_char

    final = ''.join(result)
    if final > A and final[::-1] > A:
        return final

    result = list(A)
    if result[0] < 'z':
        result[0] = chr(ord(result[0]) + 1)
        for i in range(1, N):
            result[i] = 'a'
        return ''.join(result)
    
    return "-1"

# Read input
T = int(input())
for _ in range(T):
    N = int(input())
    A = input().strip()
    print(solve_restaurant_name(N, A))