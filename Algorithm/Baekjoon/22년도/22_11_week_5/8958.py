N = int(input())
for _ in range(N):
    score = 0
    cnt = 0
    for result in input():
        if result == 'O':
            score += cnt + 1
            cnt += 1
        elif result == 'X':
            cnt = 0
    print(score)