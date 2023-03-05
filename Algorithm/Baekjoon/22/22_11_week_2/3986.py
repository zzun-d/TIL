N = int(input())
cnt = 0
for _ in range(N):
    word = input()
    stack = []
    for w in word:
        if w == 'A':
            if stack and stack[-1] == 'A':
                stack.pop()
            else:
                stack.append('A')
        else:
            if stack and stack[-1] == 'B':
                stack.pop()
            else:
                stack.append('B')
    if not stack:
        cnt += 1
print(cnt)