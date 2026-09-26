import sys

input = sys.stdin.readline

def solve():
    n, q = map(int, input().split())

    tile = [False] * (n + 1)
    color = ['a'] * (n + 1)
    last_update = [0] * (n + 1) 

    global_color = 'a'
    global_time = 0 

    for t in range(1, q + 1):
        query = input().split()

        if query[0] == '1':
            x = int(query[1])
            if not tile[x]:
                tile[x] = True
                if global_time > last_update[x]:
                    color[x] = global_color
            else:
                tile[x] = False
                last_update[x] = t
                
        else:
            global_color = query[1]
            global_time = t

    ans = []
    
    for i in range(1, n + 1):
        if not tile[i] and global_time > last_update[i]:
            ans.append(global_color)
        else:
            ans.append(color[i])

    print("".join(ans))


solve()