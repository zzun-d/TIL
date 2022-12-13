# def binary_search(l, r, n):
#     m = (l+r)//2
#     if sort_lst[m] > n:
#         r = m
#         ans = binary_search(l, r, n)
#     elif sort_lst[m] < n:

#         l = m
#         ans = binary_search(l, r, n)
#     elif sort_lst[m] == n:
#         return m
#     return ans


# N = int(input())
# lst = list(map(int, input().split()))
# sort_lst = sorted(list(set(lst)))
# ans = []
# for l in lst:
#     ans.append(binary_search(0, len(sort_lst), l))
# print(*ans)

N = int(input())
lst = list(map(int, input().split()))
sort_lst = sorted((list(set(lst))))
d = {sort_lst[i]:str(i) for i in range(len(sort_lst))}
ans = []
for l in lst:
    ans.append(d[l])
print(' '.join(ans))