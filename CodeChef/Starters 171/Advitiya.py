# cook your dish here
for _ in range(int(input())):
    
    
    s = input()
    
    n = len(s)
    
    target = "ADVITIYA"
    min_steps = 0
    for i in range(8):  
        if s[i] != target[i]:
            curr = s[i]
            steps = 0
            while curr != target[i]:
                if curr == 'Z':
                    curr = 'A'
                else:
                    curr = chr(ord(curr) + 1)
                steps += 1
            min_steps += steps
        
    print(min_steps)
