import sys
def input():
    return sys.stdin.readline().rstrip()

T = int(input())
cmds = [input().split() for _ in range(T)]
deck = []
ans = []
for c in cmds:
    if len(c) == 1:
        if c[0] == 'pop_front':
            if deck:
                ans.append(deck.pop(0))
            else:
                ans.append(-1)
        elif c[0] == 'pop_back':
            if deck:
                ans.append(deck.pop())
            else:
                ans.append(-1)
        elif c[0] == 'size':
            ans.append(len(deck))

        elif c[0] == 'empty':
            if deck:
                ans.append(0)
            else:
                ans.append(1)
        elif c[0] == 'front':
            if deck:
                ans.append(deck[0])
            else:
                ans.append(-1)
        else:
            if deck:
                ans.append(deck[-1])
            else:
                ans.append(-1)
    else:
        if len(c[0]) > 9:
            deck = [int(c[1])] + deck
        else:
            deck += [int(c[1])]
for num in ans:
    print(num)

