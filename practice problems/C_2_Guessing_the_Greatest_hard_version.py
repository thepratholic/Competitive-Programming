def query(l, r):
    print("? ", l, r, flush=True)
    x = int(input())
    return x

def left(l, r):
    pivot = r + 1
    ans = l
    while l <= r:
        mid = (l + r) >> 1
        if query(mid, pivot) == pivot:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

def right(l, r):
    pivot = l - 1
    ans = r
    while l <= r:
        mid = (l + r) >> 1
        if query(pivot, mid) == pivot:
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    return ans

def solve():
    n = int(input())
    pivot = query(1, n)

    if pivot == 1:
        pivot = right(pivot + 1, n)
    elif query(1, pivot) == pivot:  
        pivot = left(1, pivot - 1)
    else:
        pivot = right(pivot + 1, n)

    print("! ", pivot, flush=True)

solve()
