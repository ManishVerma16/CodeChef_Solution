def olympicsganking(g1,s1,b1,g2,s2,b2):
    team1 = g1+s1+b1
    team2 = g2+s2+b2
    if  team1 > team2:
        print('1')
    else:
        print('2')

try:
    t = int(input())
    while t>0:
        t -= 1
        g1, s1, b1, g2, s2, b2 = map(int, input().split())
        olympicsganking(g1,s1,b1,g2,s2,b2)
except e:
    pass

