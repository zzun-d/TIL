S = input()
ans = set()

for i in range(1, len(S) + 1):
    for j in range(len(S) + 1 - i):
        ans.add(S[j:j+i])
print(len(ans))