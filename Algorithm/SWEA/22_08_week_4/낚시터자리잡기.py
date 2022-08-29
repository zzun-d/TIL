T = int(input())

for tc in range(1, T+1):
    N = int(input())
    G = []
    place = [1]*N
    for _ in range(3):
        G.append(list(map(int, input().split())))
    
    mn = 3600

    while G:
        g, p = G.pop()

        for i in range(p):
            while True:
                if place[g-1]:
                    place[g-1] = 0
                    break
                else:
                    

    
        

    

