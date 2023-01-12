s_1 = input()
s_2 = input()

arr = [[0] * (len(s_1)+1) for _ in range((len(s_2)+ 1))]

for i in range(1, len(s_2)+1):
    for j in range(1, len(s_1)+1):
        if s_2[i-1] == s_1[j-1]:
            arr[i][j] = arr[i-1][j-1] + 1
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
print(arr[-1][-1])