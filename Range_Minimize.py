# cook your dish here
for _ in range(int(input())):
    array_size=int(input())
    array=sorted(list(map(int,input().split())))
    if array_size<=3:
        print(0)
    else:
        diff1=array[-1]-array[2]
        diff2=array[-2]-array[1]
        diff3=array[-3]-array[0]
        print(min(diff1,diff2,diff3))