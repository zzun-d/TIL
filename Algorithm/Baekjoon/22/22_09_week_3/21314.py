prob = input()
tmp = True
cnt = 0
mx = mn = ''

for p in prob:
    if p == 'K':
        mx += '5'+'0'*cnt
        if cnt:
            mn += '1' + '0'*(cnt - 1)
        mn += '5'
        cnt = 0
        continue
    cnt += 1
if cnt:
    mx += '1'*cnt
    mn += '1' + '0'*(cnt-1)
print(mx)
print(mn)