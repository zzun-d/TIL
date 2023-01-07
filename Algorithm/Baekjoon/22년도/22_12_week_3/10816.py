N= int(input())
has = {}
for n in map(int, input().split()):
    if has.get(n):
        has[n] += 1
    else:
        has[n] = 1
M = int(input())

for n in map(int, input().split()):
    if has.get(n):
        print(has[n], end=' ')
    else:
        print(0, end=' ')