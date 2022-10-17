from itertools import combinations

# 브루트포스
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
team_lst = list(combinations(range(N), N//2))
gap = 9000
for team in team_lst:
    other_team = [i for i in range(N) if i not in team]
    team_a = 0
    team_b = 0
    for i in range(N):
        if i in team:
            for idx in team:
                team_a += arr[i][idx]
        else:
            for idx in other_team:
                team_b += arr[i][idx]
    if abs(team_a - team_b) < gap:
        gap = abs(team_a - team_b)
        if gap == 0:
            break
print(gap)