N = int(input())
scores = list(map(int ,input().split()))
mx = max(scores)
sm = sum(scores)
print(sm/N*100/mx)

