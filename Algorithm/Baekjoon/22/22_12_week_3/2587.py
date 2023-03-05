sm = 0
lst = []
for _ in range(5):
    num = int(input())
    lst.append(num)
    sm += num

for i in range(4):
    for j in range(i+1, 5):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]
print(sm//5)
print(lst[2])