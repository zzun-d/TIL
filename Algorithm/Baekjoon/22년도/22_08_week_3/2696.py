import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

T = int(input())
for t in range(1, T+1):
    M = int(input())
    l, r, ans = [], [], []                  # 중앙기준 왼쪽 heap, 오른쪽 heap, 중앙값 담을 list
    print(M//2+1 if M % 2 else M//2)        # 몇개의 중앙값을 출력할 것인지

    for i in range(M//10+1 if M % 10 != 0 else M//10):      # 입력 줄 수 만큼 반복
        nums = list(map(int, input().split()))
        for idx, n in enumerate(nums):                          # 입력된 숫자 for문으로 처리
            if ans and l:                                           # 중앙값 list, 왼쪽 리스트 존재시(3번째 이상)
                if idx%2 == 0:                                          # 항상 오른쪽 heap이 왼쪽 heap보다 같거나 1개 많게 유지
                    if n >= r[0]:
                        heapq.heappush(r, n)
                    else:
                        heapq.heappush(l, -n)
                        heapq.heappush(r, -heapq.heappop(l))
                    ans.append(r[0])
                else:
                    if n >= r[0]:
                        heapq.heappush(r, n)
                        heapq.heappush(l, -heapq.heappop(r))

                    else:
                        heapq.heappush(l, -n)

            elif ans and not r:                         # 1, 2번째 각 l, r에 추가
                if nums[0] > nums[1]:
                    heapq.heappush(l, -nums[1])
                    heapq.heappush(r, nums[0])
                else:
                    heapq.heappush(l, -nums[0])
                    heapq.heappush(r, nums[1])
            else:
                ans.append(nums[0])

    for i, a in enumerate(ans, start=1):        # 출력 형식에 맞게 출력
        if i % 10:
            print(a, end=' ')
        else:
            print(a)
        if i == len(ans):
            print()
