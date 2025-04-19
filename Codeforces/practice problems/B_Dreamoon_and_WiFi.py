from math import comb 
a, b = input(), input()
n = b.count('?')
r = a.count('-') - b.count('-')
q = a.count('+') - b.count('+')
if n < r or r < 0:
    print(0)
else:
    print((comb(n, r) * comb(n - r, q)) / (2 ** n))