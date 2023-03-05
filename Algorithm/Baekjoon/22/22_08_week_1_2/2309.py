def b_sort(lst, l):
    for i in range(l):
        for j in range(0, l-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst

heights = [int(input()) for _ in range(9)]

subsets = []
for i in range(1<<9):
    subset = []
    for j in range(9):
        if i & (1<<j):
            subset.append(heights[j])
    if len(subset)==7:
        subsets.append(subset)

for subset in subsets:
    h_sum = 0
    for num in subset:
        h_sum += num
    if h_sum == 100:
        result = subset
result = b_sort(result, 7)

for num in result:
    print(num)







