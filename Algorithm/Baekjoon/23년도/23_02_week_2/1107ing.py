ch = input()
n = input()
btn = [1]*10
nums = [i for i in range(10)]
if n != '0':
    for i in map(int, input().split()):
        btn[i] = 0
        nums.remove(i)
mx_btn = str(max(nums))
mn_btn = str(min(nums))

if int(ch[0]) in nums:
    start_num = [ch[0]]
    if int(ch[0])+1 < 10 and int(ch[0])+1 in nums:
        start_num.append(str(int(ch[0])+1))
    if int(ch[0])-1 >= 0 and int(ch[0])-1 in nums:
        start_num.append(str(int(ch[0])-1))
else:
    start_num = []
    i = 1
    tmp = True
    while tmp:
        if int(ch[0])+i < 10 and int(ch[0])+i in nums:
            start_num.append(str(int(ch[0])+i))
            tmp = False
        if int(ch[0])-i >= 0 and int(ch[0])-i in nums:
            start_num.append(str(int(ch[0])-i))
            tmp = False
        i += 1


answer = []

def set_candidate(n):
    if len(n) == len(ch):
        answer.append(int(n))
        return 

    tmp = True
    target_num = int(ch[len(n)])
    i = 1
    while tmp:

        if btn[target_num]:
            set_candidate(n + ch[len(n)])
            tmp = False

        if not tmp:
            if target_num + i < 10 and btn[target_num + i]:
                answer.append(int(n+str(target_num + i) + mn_btn*(len(ch) - len(n) - 1)))

            if target_num - i >= 0 and btn[target_num - i]:
                answer.append(int(n+str(target_num - i) + mx_btn*(len(ch) - len(n) -1)))

        else:
            if target_num + i < 10 and btn[target_num + i]:
                answer.append(int(n+str(target_num + i) + mn_btn*(len(ch) - len(n) - 1)))
                set_candidate(n+str(target_num + i))
                tmp = False

            if target_num - i >= 0 and btn[target_num - i]:
                answer.append(int(n+str(target_num - i) + mx_btn*(len(ch) - len(n) -1)))
                set_candidate(n+str(target_num - i))
                tmp = False

        i+=1

cnt = 500000
for s in start_num:
    set_candidate(s)

for ans in answer:
    cnt = min(cnt, abs(int(ch) - ans) + len(str(ans)))

cnt = min(abs(int(ch) - 100), cnt)
print(answer, mx_btn)
print(cnt)