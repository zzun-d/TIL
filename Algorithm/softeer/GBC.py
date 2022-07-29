n, m = map(int, input().split())

speed_limit = []
for _ in range(n):
    d, l_s = map(int, input().split())
    speed_limit.extend([l_s] * d)

test_speed = []
for _ in range(m):
    d, l_s = map(int, input().split())
    test_speed.extend([l_s] * d)

compare_speed = []
for i in range(100):
    compare_speed.append(test_speed[i] - speed_limit[i])

print(max(max(compare_speed), 0))