import sys

def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n, x = int(data[index]), int(data[index + 1])
        index += 2
        prev, ans = 0, 0
        
        for i in range(n):
            a = int(data[index])
            index += 1
            ans = max(ans, a - prev)
            prev = a
        
        ans = max(ans, 2 * (x - prev))
        results.append(str(ans))
    
    sys.stdout.write("\n".join(results) + "\n")

if __name__ == "__main__":
    main()
