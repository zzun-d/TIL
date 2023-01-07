prob = input()
prob = prob.replace('()', '2')
prob = prob.replace('[]', '3')
p_l = []
tmp = True
for p in prob:
    if p not in [']', ')']:
        p_l.append(p)
    else:
        if p == ']' and p_l:
            nums = 0
            while p_l[-1] != '[' and len(p_l) > 1:
                if p_l[-1] == '(':
                    tmp = False
                    break
                nums += int(p_l.pop())
            if p_l and p_l[-1] == '[':
                p_l.pop()
            else:
                tmp = False
                break
            nums *= 3
            p_l.append(str(nums))
                
        elif p == ')' and p_l:
            nums = 0
            while p_l[-1] != '(' and len(p_l) > 1:
                if p_l[-1] == '[':
                    tmp = False
                    break
                nums += int(p_l.pop())
            if p_l and p_l[-1] == '(':
                p_l.pop()
            else:
                tmp = False
                break
            nums *= 2
            p_l.append(str(nums))
        else:
            tmp = False
            break
    if not tmp:
        break

for p in p_l:
    if p in ['[', ']', '(', ')']:
        tmp = False
if tmp:
    p_l = map(int, p_l)
    print(sum(p_l))
else:
    print(0)

