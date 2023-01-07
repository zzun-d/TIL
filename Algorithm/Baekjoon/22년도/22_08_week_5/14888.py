def dfs(v, A):              # dfs
    global cal
    if sum(cal) == 0:           # 연산자 모두 썼으면,
        ans.append(v)               # 결과값 ans에 append
        return

    for i in range(4):          # 연산자 for 루프
        if cal[i]:                  # 연산자가 있으면,
            V = v                       # v함수 임시 저장
            AA = A[:]                   # A리스트 임시 저장
            if i == 0:                  # 연산 실행
                v += A.pop()
            elif i == 1:
                v -= A.pop()
            elif i == 2:
                v *= A.pop()
            else:
                if v >= 0:
                    v = v // A.pop()
                else:
                    v = -((-v)//A.pop())

            cal[i] -= 1                 # 해당 연산자 -= 1
            dfs(v, A)                   # 재귀
            cal[i] += 1                 # for 루프를 위한 원상복구
            v = V
            A = AA

N = int(input())
An = list(map(int, input().split()))
cal = list(map(int, input().split()))
An.reverse()    # deque 안쓰고 pop 효율적으로 하기 위해 reverse
a = An.pop()    # 첫 연산 숫자
ans = []
dfs(a, An)
print(max(ans))
print(min(ans))