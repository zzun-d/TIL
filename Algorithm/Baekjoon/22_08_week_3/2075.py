import sys
import heapq

def input():
    return sys.stdin.readline().rstrip()

N = int(input())
heap = []

for i in range(N):
    for num in list(map(int, input().split())):     # 숫자들을 heap에 push
        heapq.heappush(heap, num)
    while len(heap) > N:                            # heap 길이가 N을 초과하면 N이 될 때까지 pop
        heapq.heappop(heap)


print(min(heap))        # heap의 길이가 N과 같으므로 최솟값이 N번째로 큰 값

