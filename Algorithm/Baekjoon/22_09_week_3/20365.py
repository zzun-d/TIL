N = int(input())
prob = input()
result_B = result_R = 1
tmp = False
for p in prob:
    if p == 'R':
        if tmp:
            continue
        else:
            result_R += 1
            tmp = True
    else:
        tmp = False


tmp = False
for p in prob:
    if p == 'B':
        if tmp:
            continue
        else:
            result_B += 1
            tmp = True
    else:
        tmp = False

print(min(result_B, result_R))
