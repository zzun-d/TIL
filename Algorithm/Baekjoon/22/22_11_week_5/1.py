D = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
word = input()
cost = 0
for w in word:
    for i in range(8):
        if w in D[i]:
            cost += i+3
            break
print(cost)