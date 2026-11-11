def binary_deque():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        
        total = sum(a)
        
        if total < s:
            print(-1)
            continue
        if total == s:
            print(0)
            continue
        
        left = 0
        current_sum = 0
        max_len = -1
        
        for right in range(n):
            current_sum += a[right]
            
            while current_sum > s:
                current_sum -= a[left]
                left += 1
            
            if current_sum == s:
                max_len = max(max_len, right - left + 1)
        
        print(n - max_len)

binary_deque()
