def f(i, n):
    if i == n + 1:
        return
    
    print(i)

    f(i + 1, n)
    return

f(1, 5)