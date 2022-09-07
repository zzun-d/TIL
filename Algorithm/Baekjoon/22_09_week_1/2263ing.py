import sys
sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline().rstrip()

def tree(in_start, in_end, post_start, post_end):           # 전위 순회 출력하는 함수
    if in_start > in_end or post_start > post_end:              # 중위 순회, 후위 순회 중 하나라도 시작 인덱스가 종료 인덱스보다 크면 종료
        return
    
    r = postord[post_end]                  # root값(후위 순회의 마지막 노드가 루트노드) 
    print(r, end=' ')                       # root 출력

    left_tree = tree_idx[r] - in_start      # root의 중위 순회에서의 idx 기준으로 좌측은 좌측 tree,
    right_tree = in_end - tree_idx[r]       # 우측은 우측 tree로 정의

    tree(in_start, in_start + left_tree - 1, post_start, post_start + left_tree - 1)    # 좌측 트리부터 재귀를 통해 루트 값 계속 프린트
    tree(in_end - right_tree + 1, in_end, post_end - right_tree, post_end-1)
 



N = int(input())
inord = list(map(int, input().split()))        # 중위 순회
postord =  list(map(int, input().split()))     # 후위 순회

tree_idx = [0] * (N+1)                          # node값의 중위 순회 index를 저장하기 위한 리스트

for i in range(N):                              # 노드의 중위 순회 인덱스 저장
    tree_idx[inord[i]] = i

tree(0, N-1, 0, N-1)
