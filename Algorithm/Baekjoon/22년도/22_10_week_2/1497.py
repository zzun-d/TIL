from itertools import combinations

N, M = map(int, input().split())
pos_play = []           # 연주 가능한 곡 정보 넣을 리스트

# 곡 정보 set으로 0부터 M-1까지 pos_play에 append
for _ in range(N):      
    s = set()
    _, pos = input().split()

    for i in range(M):
        if pos[i] == 'Y':
            s.add(i)
    pos_play.append(s)

k = 1                   # 고를 기타 개수
tmp = False             # while문 탈출 플래그
sm = set()              # 최대 가능 곡 개수 확인용 변수

for p in pos_play:      # 모든 가능 곡 합집합
    sm |= p

mx = len(sm)            # 최대 가능 곡 수

if mx:                  # 만약 연주 가능한 곡이 있으면 
    while k <= N:           # 고르는 기타 개수가 총 기타 개수보다 작거나 같으면 루프
        for l in combinations(pos_play, k):         # 가능한 연주곡 목록에서 k개 만큼 뽑는다
            pp = set()
            for s in l:                             # 합집합
                pp |= s
            if len(pp) == mx:                       # 연주 가능 곡 수가 최대 가능 곡 수와 같으면 tmp True, break
                tmp = True
                break

        if tmp:
            break

        k += 1              # 기타 고르는 개수 +1

if tmp:                 # 연주 가능하면 k 값 프린트
    print(k)
else:                   # 불가능시 -1 프린트
    print(-1)