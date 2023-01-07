import sys
def input():
    return sys.stdin.readline().rstrip()

N, M = map(int, input().split())
book = {i:input() for i in range(1, N+1)}
b_v = list(book.values())
b_k = list(book.keys())
book_2 = {b_v[i]:b_k[i] for i in range(N)}
ans = []
for i in range(M):
    prob = input()
    if prob.isdigit():
        ans.append(book[int(prob)])
    else:
        ans.append(book_2[prob])
for i in ans:
    print(i)
