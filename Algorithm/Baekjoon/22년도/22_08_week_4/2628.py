W, H = map(int, (input().split()))

cut = int(input())
w_c = [0, H]            # 가로 컷 인덱스
h_c = [0, W]            # 세로 컷 인덱스

for _ in range(cut):        # 가로 컷인지 세로 컷인지 구분하여 append
    wh, idx = map(int, input().split())
    if wh:
        h_c.append(idx)
    else:
        w_c.append(idx)

w_c.sort()          # 오름차순 정렬
h_c.sort()

w_mx = h_mx = 0     # 인덱스 사이 길이 최대 값 초기화

for i in range(len(w_c)-1):     # 가로컷 인덱스 사이 크기 최댓값 갱신
    w = w_c[i+1] - w_c[i]
    if w > w_mx:
        w_mx = w

for i in range(len(h_c)-1):     # 세로컷 인덱스 사이 크기 최댓값 갱신
    h = h_c[i+1] - h_c[i]
    if h > h_mx:
        h_mx = h

print(w_mx * h_mx)