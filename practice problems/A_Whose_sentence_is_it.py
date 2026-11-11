n=int(input())
for i in range(n):
    s=input()
    if s[0:5]=='miao.' and s[-5:]!='lala.':print('Rainbow\'s')
    elif s[0:5]!='miao.' and s[-5:]=='lala.':print('Freda\'s')
    else:print('OMG>.< I don\'t know!')