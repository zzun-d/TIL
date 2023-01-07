N = int(input())
cnt = 0
for _ in range(N):
    alphas = 'abcdefghijklmnopqrstuvwxyz'
    word = input()
    a = word[0]
    tmp = True
    for i in range(1, len(word)):
        if word[i] == a:
            continue
        alphas = alphas.replace(a, '')
        if alphas.find(word[i]) == -1:
            tmp = False
            break
        a = word[i]

    if tmp:
        cnt += 1

print(cnt)