N = int(input())

mx_cnt = 0                      # 최대 길이 변수
mx_lst = []                     # 최대 길이 때의 정수들 리스트
for i in range(N//2, N+1):      # N의 절반부터 N까지 루프
    lst = [N, i]                
    cnt = 2                     
    while lst[-2] - lst[-1] >= 0:       # 앞수에서 뒷수 뺀 값이 0보다 크거나 같으면 리스트에 append 반복
        cnt += 1
        lst.append(lst[-2] - lst[-1])
    if cnt > mx_cnt:                    # cnt가 나온 최대 횟수보다 크면 갱신
        mx_cnt = cnt
        mx_lst = lst

print(mx_cnt)
print(*mx_lst)