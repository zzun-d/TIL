for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    
    for _ in range(dump):
        boxes.sort()
        boxes[0] += 1
        boxes[-1] -= 1
    boxes.sort()

    print(f'#{t} {boxes[-1] - boxes[0]}')