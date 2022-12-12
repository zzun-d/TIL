def find(n):
    if n != lst[n]:
        lst[n] = find(lst[n])
    return lst[n]

N = int(input())
M = int(input())
lst = [i for i in range(N)]
for i in range(N):
    connect = list(map(int, input().split()))
    for j in range(N):
        if connect[j] == 1:
            lst[find(j)] = find(i)
cities = list(map(int, input().split()))
tmp = find(cities[0] - 1)
for city in cities[1:]:
    if tmp != find(city-1):
        print('NO')
        break
else:
    print('YES')