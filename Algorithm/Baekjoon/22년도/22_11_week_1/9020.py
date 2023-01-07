def prime(n):
    k = int(n**0.5)         # 주어진 수의 제곱근 값부터 시작
    while k > 1:            # 나눠주는 수가 1보다 크면 계속 루프
        if n % k == 0:          # 나눠지면 소수 아님 False 리턴
            return False
        k -= 1                  # 나누는 수 -1
    return True             # 무사 통과 시 소수! True 리턴


T = int(input())
for _ in range(T):
    N = int(input())
    small_num = N//2                # N을 이루는 수 중 작은 수
    while True:
        if prime(small_num) and prime(N - small_num):   # 작은 수 큰 수 모두 소수면 출력 &  break
            print(small_num, N-small_num)
            break
        
        else:                                           # 아니면 작은 수 -1
            small_num -= 1