t = int(input())
while t > 0:
    n, k, x, y = input().split(" ")
    n = int(n)
    k = int(k)
    x = int(x)
    y = int(y)
    day = 0
    while True:
        new_city = (k+x)%n
        if new_city == y:
            print("YES")
            break
        else:
            x = new_city
            day += 1
            if day < 100000:
                print("NO")
                break
    t -= 1