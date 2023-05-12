part1 = input()
part2 = input()

if len(part2) > len(part1):
    part1, part2 = part2, part1
l1 = len(part1)
l2 = len(part2)

ans = l1 + l2

print(l1, l2)
for i in range(1, l1 + l2):
    tmp = True
    if i <= l2:
        for j in range(i):
            if part1[i-j-1] == '2' and part2[-(j-1)] == '2':
                tmp = False
                break
    else:
        for j in range(l2):
            if part1[j + l2 - i] == '2' and part2[j] == '2':
                tmp = False
                break
    if tmp:
        print(i, ans)
        if i >= l2 and i <= l1-l2:
            ans = l1
            break
        else:
            ans = min(l1 + l2 - i, l1 + l2 + l1 - i)
print(ans)
