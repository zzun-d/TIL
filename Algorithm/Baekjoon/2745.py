n, b = input().split()
n = list(n)
b = int(b)

# 11진법부터 알파벳 숫자로 변환하는 dict 생성
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
trans_dict = {alpha[i]:i+10 for i in range(26)}

# 10진법 넘어가면 위 dict로 알파벳 숫자로 변환
# 후 int타입으로 list저장
if b > 10:
    for idx, num in enumerate(n):
        if num.isalpha():
            n[idx] = trans_dict[num]
        else:
            n[idx] = int(num)
else:
    n = list(map(int, n))

trans_num = 0

# 리스트 거꾸로 돌려서 맨 뒤 숫자부터 10진법 변환
n.reverse()
for idx, num in enumerate(n):
    trans_num += (b ** idx) * num

print(trans_num)
