nums = set(list(range(1, 10001)))
def d(n):
    global nums

    if nums.intersection({n}):
        
        nxt_n = n
        while n:
            nxt_n += n%10
            n = n//10
        if nxt_n <= 10000:
            d(nxt_n)
            nums -= {nxt_n}
    return

for i in range(1, 10001):
    d(i)
nums = sorted(list(nums))
for num in nums:
    print(num)