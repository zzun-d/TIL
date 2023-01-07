def f(a, b):
    while a % b:
        a, b = b, a%b
    return b

N = int(input())

lst = list(map(int, input().split()))
s = lst[0]
for n in lst[1:]:
    mx = f(max(s, n), min(s, n))
    print(f'{s//mx}/{n//mx}')
    