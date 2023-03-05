A, B, V = map(int, input().split())
x = A - B
V -= A
if V%x:
    print(V//x + 2)
else:
    print(V//x + 1)

