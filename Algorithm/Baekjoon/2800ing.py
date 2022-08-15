prob = input()
ans = []
p_l = []

for idx, p in enumerate(prob):
    if p == '(':
        p_l.append(idx)
    elif p == ')':
        ans.append((p_l.pop(), idx))
print(ans)

for i in range(1<<5):
    pass