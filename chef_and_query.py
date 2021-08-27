n, k = input().split()
n = int(n)
k = int(k)
day = 0
remain_query = 0
queries = list(map(int, input().split()))
for i in range(len(queries)-1):
    if queries[i] + remain_query < k:
        exit
    else:
        remain_query = queries[i] - k
        queries[i+1] += remain_query
        day += 1
print(day+1)
