T = int(input())
for i in range(T):
    word = input()
    answer = 1
    for j in range(len(word)//2):
        if word[j] != word[-1-j]:
            answer = 0
    print('#{} {}'.format(i+1, answer))