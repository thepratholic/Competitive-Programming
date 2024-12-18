# cook your dish here
for _ in range(int(input())):
    
    x = int(input())
    
    if x <= 100:
        print(x)
    elif 100 < x <= 1000:
        print(x - 25)
        
    elif x > 1000 and x <= 5000:
        print(x - 100)
        
    elif x > 5000:
        print(x - 500)