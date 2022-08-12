import sys
def input():
    return sys.stdin.readline().rstrip()

prob = input()
pipes = 0
ans = 0
for i in range(len(prob)-1):
    if prob[i] == ')' and prob[i-1] == '(':
        continue
    elif prob[i] == '(' and prob[i+1] == ')':
        ans += pipes
    elif prob[i] == '(':
        pipes += 1
        ans += 1
    else:
        pipes -= 1
print(ans)