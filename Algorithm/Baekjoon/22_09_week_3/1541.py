prob = input()
stack_pos = 0
stack_neg = 0
num = ''
tmp = True
for c in prob:
    if tmp:
        if c == '-':
            tmp = False
            stack_pos += int(num)
            num = ''
        elif c == '+':
            stack_pos += int(num)
            num = ''
        else:
            num += c
    else:
        if c not in ['-','+']:
            num += c
        else:
            stack_neg += int(num)
            num = ''
if tmp:
    stack_pos += int(num)
else:
    stack_neg += int(num)
print(stack_pos-stack_neg)