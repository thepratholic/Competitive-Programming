# cook your dish here
for _ in range(int(input())):
    
    x, y = map(int, input().split())
    
    half_one = x // 2
    half_two = y // 2
    
    first_half = "1" * half_one + "2" * half_two
    palin = first_half + first_half[::-1]
    
    print(palin)