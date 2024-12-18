# cook your dish here
for _ in range(int(input())):
    
    n, x = map(int, input().split())
    
    pizza = (n * x) // 4
    
    if (n * x) % 4 == 0:
        print(pizza)

    else:
        print(pizza + 1)