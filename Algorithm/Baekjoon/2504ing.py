prob = input()
prob = prob.replace('()', '2')
prob = prob.replace('[]', '3')
p_l = []
result = 0
ans = 0
while True:
    for p in prob:
        if p.isdigit():
            p = int(p)
            ans += p
        elif p == '(' or p == '[':
            p_l.append(p)
        else:
            if not p_l:
                result = 0
                break
            elif p == ')' and p_l[-1] == '(':
                p_l.pop()
                result += ans * 2
            elif p == ']' and p_l[-1] == '[':
                p_l.pop()
                result += ans * 3