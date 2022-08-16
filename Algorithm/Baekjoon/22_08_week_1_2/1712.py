a, b, c = map(int, input().split())

# 노트북 1대 생산비용이 1대 판매비용보다 크거나 같으면 이익이 없음
if b >= c:
    print(-1)

# 대당 판매 이익을 초기 고정비용을 넘어가는 만큼을 출력
else:  
    benefit = c - b
    print(a // benefit + 1)