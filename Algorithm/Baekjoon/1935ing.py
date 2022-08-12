N = int(input())
S = input()

alp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

alp_num = {alp[i]:int(input()) for i in range(N)}
i = 0
while i < len(S):
    nums = []
    cal = []
    while S[i] in alp and i < len(S):
        nums.append(alp_num[S[i]])
        i += 1
    while S[i] not in alp and i < len(S):
        cal.append()