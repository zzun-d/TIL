N = int(input())
ans = 1
s = 0
n = 1

for i in range(2, 1 + int((2*N)**0.5)):     # 대충 근의공식에 의한 최대 합의 길이까지 루프
    k = 0       
    
    # N을 숫자 갯수로 나눈 몫에서 숫자 절반 만큼 뺀 인덱스부터 숫자 갯수 만큼 더함
    # 그 값이 N보다 크거나 같으면 break
    # 아니면 한 숫자씩 증가해 가면서 더함
    while True:                        
        sm = sum(range(N//i - i//2 + k, N//i - i//2 + i + k))
        if sm >= N:
            break
        else:
            k += 1
    if sm == N:
        ans += 1


print(ans)