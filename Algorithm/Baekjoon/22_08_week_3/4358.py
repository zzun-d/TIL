import sys
tree_dict = {}
cnt = 0
while True:     # 입력이 끝날 때 까지 루프
    tree = sys.stdin.readline().rstrip()
    if not tree:                # 입력이 들어오지 않으면 break
        break
    if tree_dict.get(tree):     # tree_dict에 이미 등록된 나무면 + 1
        tree_dict[tree] += 1
    else:                       # tree_dict에 등록되지 않은 나무면 등록
        tree_dict[tree] = 1
    cnt += 1                    # 토탈 나무 카운팅

k_list = list(tree_dict.keys())     # dict의 key를 list로 만들어 정렬
k_list.sort()
for k in k_list:
    print(f'{k} {tree_dict[k]/cnt*100:.4f}')    # 소수점 4째자리 까지 출력
