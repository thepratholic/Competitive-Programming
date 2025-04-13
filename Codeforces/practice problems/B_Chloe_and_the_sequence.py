def find_element(n, k):
    if n == 1:
        return 1
    mid = 1 << (n - 1) 
    
    if k == mid:
        return n
    elif k < mid:
        return find_element(n - 1, k)
    else:
        return find_element(n - 1, k - mid)

n, k = map(int, input().split())
print(find_element(n, k))
