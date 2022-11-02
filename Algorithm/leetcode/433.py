from collections import deque
                
def check(s1, s2):
    cnt = 0
    for i in range(8):
        if s1[i] != s2[i]:
            cnt += 1
    if cnt == 1:
        return True
    else:
        return False

start = input()
end = input()
bank = list(input().split())


q = deque([(start, 0)])
result = -1
while q:
    s, cnt = q.popleft()
    remove_lst = []
    for b in bank:
        if check(s, b):
            if b == end:
                result = cnt + 1
                q = False
                break
            else:
                q.append((b, cnt+1))
            remove_lst.append(b)
    for r in remove_lst:
        bank.remove(r)

print(result)


