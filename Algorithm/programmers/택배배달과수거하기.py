def solution(cap, n, deliveries, pickups):
    def check(n, lst):
        if n == 0:
            return 0
        while lst[n] == 0:
            n -= 1
            
        return max(n, 0)
        
    
    answer = 0
    deliv = check(len(deliveries) - 1, deliveries)
    pickup = check(len(pickups) - 1, pickups)

    while deliv > 0 or pickup > 0:
        deliv_cnt = pickup_cnt = cap
        answer += (max(deliv, pickup) + 1) * 2
        
        while deliv_cnt > 0 and deliv > 0:
            if deliveries[deliv] >= deliv_cnt:
                deliveries[deliv] -= deliv_cnt
                deliv = check(deliv, deliveries)
                deliv_cnt = 0
            else:
                deliv_cnt -= deliveries[deliv]
                deliveries[deliv] = 0
                deliv = check(deliv, deliveries)
                
        while pickup_cnt > 0 and pickup > 0:
            if pickups[pickup] >= pickup_cnt:
                pickups[pickup] -= pickup_cnt
                pickup = check(pickup, pickups)
                pickup_cnt = 0
            else:
                pickup_cnt -= pickups[pickup]
                pickups[pickup] = 0
                pickup = check(pickup, pickups)
                
        
    return answer

print(solution(4, 5, [1, 0, 3, 1, 2], [0, 3, 0, 4, 0]))