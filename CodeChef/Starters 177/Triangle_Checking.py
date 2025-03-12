def solve():
    a, b, c = map(int, input().split())

    if (a + b > c) and (b + c > a) and (a + c > b):
        print("Yes")
        return
    else:
        print("No")
        return
    
if __name__ == "__main__":
    solve()