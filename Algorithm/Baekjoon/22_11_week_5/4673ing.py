nums = set(list(range(1, 101)))
def d(n):
    global nums
    if nums.intersection({n}):
        
        nxt_n = n
        while n:
            nxt_n += n%10
            n = n//10
        nums -= {nxt_n}
        if nxt_n <= 100:
            d(nxt_n)
    return
for i in range(1, 101):
    d(i)
print(len(nums))
