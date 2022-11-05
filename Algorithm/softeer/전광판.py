nums = {
    '0' : (1, 1, 1, 0, 1, 1, 1),
    '1' : (0, 0, 1, 0, 0, 0, 1),
    '2' : (0, 1, 1, 1, 1, 1, 0),
    '3' : (0, 1, 1, 1, 0, 1, 1),
    '4' : (1, 0, 1, 1, 0, 0, 1),
    '5' : (1, 1, 0, 1, 0, 1, 1),
    '6' : (1, 1, 0, 1, 1, 1, 1),
    '7' : (1, 1, 1, 0, 0, 0, 1),
    '8' : (1, 1, 1, 1, 1, 1, 1),
    '9' : (1, 1, 1, 1, 0, 1, 1),
    }

t = int(input())

for _ in range(t):
    old_num, new_num = input().split()
    swich_cnt = 0
    while True:
        if len(old_num) == 0 or len(new_num) == 0:
            new_num = old_num + new_num
            for n in new_num:
                swich_cnt += sum(nums[n])
            break
        num_1 = nums[old_num[-1]]
        num_2 = nums[new_num[-1]]
        for i in range(7):
            if num_1[i] != num_2[i]:
                swich_cnt += 1
        old_num = old_num[:-1]
        new_num = new_num[:-1]
    
    print(swich_cnt)
