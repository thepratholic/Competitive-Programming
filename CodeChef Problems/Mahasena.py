# cook your dish here
N = int(input())
    
arr = list(map(int, input().split()))
notReady = 0
ready = 0
for i in arr:
    if i % 2 == 0:
        ready += 1
    else:
        notReady += 1
        
if ready > notReady: print("READY FOR BATTLE")
elif ready < notReady: print("NOT READY")
elif ready == notReady:
    print("NOT READY")