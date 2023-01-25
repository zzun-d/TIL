N = int(input())
s = set(input().split())

M = int(input())
for m in input().split():
    if s.intersection({m}):
        print(1)
    else:
        print(0)