prob = input()
bracket_sign = []
bracket_num = []
sign = []
num = []
b_s = 0
tmp = 0
out_tmp = False
for p in prob:
    if p == '(':
        b_s += 1
        continue
# A+B*C-D/E
    if b_s:
        if p.isalpha():
            if tmp == b_s:
                bracket_num.append(bracket_num.pop()+p+bracket_sign.pop())
                tmp -= 1
            else:
                bracket_num.append(p)
        elif p != ')':
            if p in ['*', '/']:
                tmp = b_s
                bracket_sign.append(p)
            else:
                bracket_sign.append(p)
        else:
            b_s -= 1
            if b_s and not tmp:
                if bracket_sign:
                    bracket_num.append(bracket_num.pop(-2) + bracket_num.pop() + bracket_sign.pop())
        
            elif b_s and tmp:
                bracket_num.append(bracket_num.pop()+bracket_sign.pop())
            else:
                num.append(''.join(bracket_num) + ''.join(bracket_sign[::-1]))
                if sign:
                    num.append(num.pop(-2) + num.pop() + sign.pop())
                bracket_num = []
                bracket_sign = []
    else:
        if p.isalpha():
            if out_tmp:
                num.append(num.pop() + p + sign.pop())
                if sign:
                    num.append(num.pop(-2) + num.pop() + sign.pop())
                out_tmp = False
            else:
                num.append(p)
        else:
            if p in ['*', '/']:
                out_tmp = True
                sign.append(p)
            else:
                sign.append(p)


print(''.join(num) + ''.join(sign[::-1]))