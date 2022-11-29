mx = 0
for i in range(1, 10):
    num = int(input())
    if num > mx:
        mx = num
        mx_idx = i
print(f'{mx}\n{mx_idx}')