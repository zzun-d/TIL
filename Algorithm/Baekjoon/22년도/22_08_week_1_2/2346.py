import sys
def input():
    return sys.stdin.readline().rstrip()


N = int(input())
nums = list(map(int, input().split()))

# 풍선 고유번호와 쪽지번호 튜플로 묶음
bal_num = [(i, nums[i-1]) for i in range(1, N+1)]

# 터진 풍선 고유번호 넣을 ans 생성
ans = []
boom = 0 # 터질 풍선 자리

for i in range(1, N):
    idx, mv = bal_num.pop(boom)
    if boom >= 0:   
        bal_num = bal_num[boom:] + bal_num[:boom]
    else:
        bal_num = bal_num[boom+1:] + bal_num[:boom+1]
    ans.append(idx)
    if mv > 0:  # 쪽지번호가 양수
        mv -= 1 # 리스트 인덱스는 0부터 시작하기 때문에
        boom = mv % (N-i)
    else:
        boom = mv % -(N-i)
ans.append(bal_num[0][0])
print(*ans)


    
