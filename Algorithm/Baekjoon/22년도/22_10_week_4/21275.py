A, B = input().split()
mxA = mxB = 0
for a in A:
    mxA = max(mxA, ord(a))
for b in B:
    mxB = max(mxB, ord(b))

if chr(mxA).isalpha():
    a_n = mxA - 87
else:
    a_n = int(chr(mxA))

if chr(mxB).isalpha():
    b_n = mxB - 87
else:
    b_n = int(chr(mxB))
cnt = 0
ans = 0
for i in range(a_n+1, 37):
    for j in range(b_n+1, 37):
        if i == j:
            continue
        a_value = b_value = 0
        for idx in range(len(A)):
            if A[-1 - idx].isalpha():
                a_value += (ord(A[-1 - idx]) - 87) * (i**idx)
            else:
                a_value += int(A[-1 - idx]) * (i**idx)
        for idx in range(len(B)):
            if B[-1 - idx].isalpha():
                b_value += (ord(B[-1 - idx]) - 87) * (j**idx)
            else:
                b_value += int(B[-1 - idx]) * (j**idx)
        if a_value == b_value and a_value < 2**63:
            cnt += 1
            ans = [a_value, i, j]

if cnt == 0:
    print('Impossible')
elif cnt == 1:
    print(*ans)
else:
    print('Multiple')
