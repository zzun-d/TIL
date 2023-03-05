def dfs(s, lst):
    if len(s) == len(S):
        print(s)
    
    for i in range(26):
        if lst[i]:
            lst[i] -= 1
            dfs(s+alpha[i], lst)
            lst[i] += 1
            

alpha = 'abcdefghijklmnopqrstuvwxyz'



N = int(input())
for _ in range(N):
    alpha_nums = [0] * 26
    S = input()
    l_S = len(S)
    for s in S:
        alpha_nums[alpha.index(s)] += 1
    dfs('', alpha_nums)

    


