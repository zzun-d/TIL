T = int(input())

for tc in range(1, T+1):
    nums = input()
    l = len(nums)
    v = 0
    for i in range(l):
        if ord(nums[i]) - 64 < 0:
            v += int(nums[i]) * (16 ** (l-(i+1)))
        else:
            v += (ord(nums[i]) - 54) * (16 ** (l-(i+1)))
    p = []
    while v:
        p.append(v%2)
        v = v//2
    print(p)

