def cricketRanking(r1,w1,c1,r2,w2,c2):
    count = 0
    if r1 > r2 :
        count += 1
    else:
        count -= 1

    if c1 > c2:
        count += 1
    else:
        count -= 1

    if w1 > w2:
        count += 1
    else:
        count -= 1

    return count

try:
    t = int(input())
    while t>0:
        t -= 1
        r1, w1, c1 = map(int, input().split())
        r2, w2, c2 = map(int, input().split())
        res = cricketRanking(r1,w1,c1,r2,w2,c2)
        if res > 0:
            print("A")
        else:
            print("B")
except e:
    pass

