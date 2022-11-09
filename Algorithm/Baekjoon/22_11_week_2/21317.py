N = int(input())
graph = [list(map(int, input().split())) for _ in range(N-1)]
K = int(input())
dp_1 = [0]*(N)      # 매우 큰 점프 남아있는 dp 배열
dp_2 = [0]*(N)      # 매우 큰 점프 없는 dp 배열

if N == 1:          # 돌 갯수 1개면 그자리
    print(0)

elif N == 2:        # 돌 갯수 2개면 작은 점프
    print(graph[0][0])

elif N == 3:        # 돌 갯수 3개면 작은 점프 2번 or 큰 점프 한번
    print(min(graph[0][0] + graph[1][0], graph[0][1]))

else:
    dp_1[1] = graph[0][0]
    dp_1[2] = min(graph[0][0] + graph[1][0], graph[0][1])       # 1칸, 2칸 초기화

    for i in range(3, N):               
        dp_1[i] = min(dp_1[i-1] + graph[i-1][0], dp_1[i-2] + graph[i-2][1])     # 직전 돌, 직직전 돌 까지 비용 + 점프 비용 중 적은 비용 채택
        dp_2[i] = dp_1[i-3] + K                                                 # 아주 큰 점프 비용 갱신
        if dp_2[i-2]:                                                           # 직직전 아주 큰 점프 한 후 배열에 값이 있으면 미니멈 갱신
            dp_2[i] = min(dp_2[i-2] + graph[i-2][1], dp_2[i])
            
        if dp_2[i-1]:                                                           # 직전 아주 큰 점프 한 후 배열에 값이 있으면 미니멈 갱신
            dp_2[i] =  min(dp_2[i-1] + graph[i-1][0], dp_2[i])

    print(min(dp_1[-1], dp_2[-1]))                              # 아주 큰 점프 사용한 배열, 안사용한 배열 중 적은 값 반환