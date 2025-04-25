s = int(input())
for _ in range(s):
	n, l, r = map(int,input().split(" "))
	a = list(map(int,input().split(" ")))
	i = 0
	j = 0
	a.sort()
	count = 0
	while i < n:
		n -= 1
		while i < n and a[i] + a[n] < l:
			i += 1
		while j < n and a[j] + a[n] <= r:
			j += 1
		count += min(n,j) - i
		
	print(count)