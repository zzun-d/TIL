N = int(input())
work = []
move = []
for _ in range(N-1):
    work_a, work_b, a_to_b, b_to_a = map(int, input().split())
    work.append((work_a, work_b))
    move.append((a_to_b, b_to_a))   
work.append(list(map(int, input().split())))

dp_a = [0] * N
dp_b = [0] * N

dp_a[0] = work[0][0]
dp_b[0] = work[0][1]

for i in range(1, N):
    dp_a[i] = min(dp_a[i-1], dp_b[i-1] + move[i-1][1]) + work[i][0]
    dp_b[i] = min(dp_b[i-1], dp_a[i-1] + move[i-1][0]) + work[i][1]

print(min(dp_a[-1], dp_b[-1]))