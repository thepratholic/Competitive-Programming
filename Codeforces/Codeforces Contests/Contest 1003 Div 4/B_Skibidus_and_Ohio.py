def solve():
    s = input()

    for i in range(len(s) - 1):
        if s[i] == s[i+1]:
            print(1)
            return
        
    print(len(s))

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()