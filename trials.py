def f(a, n):
    if n == 1:
        return a
    
    ans = f(a, n - 1)
    return a * ans

print(f(2, 4))