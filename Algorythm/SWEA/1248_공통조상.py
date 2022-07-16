T = int(input())
for t in range(T):
    N, _, A, B = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    tri_map = {}
    for i in range(0,len(nums),2):
        if nums[i] not in list(tri_map.keys()):
            tri_map[nums[i]] = [nums[i+1]]
        else:
            tri_map[nums[i]].append(nums[i+1])
    tri_list = list(tri_map.items())
    top_A = set()
    top_B = set()
    while True:
        for k, v in tri_list:
            if A in v:
                top_A.add(k)
                A = k
            if B in v:
                top_B.add(k)
                B = k
        if top_B & top_A:
            break

    top = max(top_A & top_B)
    p = top
    child = tri_map[top]
    sub_tris = len(child) + 1
    
    while True:
        child_update = []    
        for k in child:
            if k in tri_map.keys():
                sub_tris += len(tri_map[k])
                child_update.extend(tri_map[k])
        child = child_update
        if len(child) < 1:
            break
            

    print(f'#{t+1} {top} {sub_tris}')

    

