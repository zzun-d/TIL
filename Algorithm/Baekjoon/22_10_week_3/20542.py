n, m = map(int, input().split())
w1 = input()
w2 = input()

edit_table = [[0]*(len(w1)+1) for _ in range(len(w2)+1)]

for i in range(len(w1) + 1):
    edit_table[0][i] = i

for i in range(len(w2) + 1):
    edit_table[i][0] = i

for i in range(1, len(w2) + 1):
    for j in range(1, len(w1) + 1):
        if w1[j-1] == w2[i-1] or (w1[j-1] == 'i' and w2[i-1] in 'jl') or w1[j-1] == 'v' and w2[i-1] == 'w':
            edit_table[i][j] = edit_table[i-1][j-1]
        else:
            edit_table[i][j] = min(edit_table[i-1][j] + 1, edit_table[i][j-1] + 1, edit_table[i-1][j-1] + 1)

print(edit_table[-1][-1])