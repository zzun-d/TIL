def check(arr):
    std = arr[0]
    for ele in arr:
        if ele != std:
            return False
    return True


def div(arr):
    global w, b

    if check(arr):
        if arr[0]:
            b += 1
        else:
            w += 1

    else:
        l = round(len(arr)**0.5)
        arr1 = []
        arr2 = []
        arr3 = []
        arr4 = []
        for i in range(l//2):

            arr1 += arr[l*i:(l*i) + l//2]
            arr2 += arr[l*i+l//2:(i+1)*l]
            arr3 += arr[((l//2)+i)*l:((l//2)+i)*l + l//2]
            arr4 += arr[((l//2)+i)*l + l//2:(((l//2)+i)+1)*l]
        div(arr1)
        div(arr2)
        div(arr3)
        div(arr4)


N = int(input())
arr = []
for _ in range(N):
    arr += list(map(int, input().split()))
w = b = 0

div(arr)
print(w)
print(b)
