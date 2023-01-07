def f(n):
    ans = set()
    for i in range(1, int(n**0.5)+2):
        if n % i == 0:
            ans.add(i)
            ans.add(n//i)
    return ans

a, b = map(int, input().split())
mx = max(f(a) & f(b))
print(mx)
print((b//mx)*a)