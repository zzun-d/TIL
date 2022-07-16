T= int(input())
for i in range(T):
    print(f'#{i+1}')
    N = int(input())
    n_l = [input().split() for _ in range(N)]
    spin_l = []
    for l in range(3):
        for j in range(N):
            for k in range(N):
                spin_l.append(n_l[-k-1][j])
        n_l = [spin_l[j*N+l*N**2:j*N+N+l*N**2] for j in range(N)]
    spin_l = [''.join(spin_l[j*N**2 + k*N:j*N**2+N + k*N]) for k in range(N) for j in range(N)]
    for l in range(N):
        print(' '.join(spin_l[l*N:(l+1)*N]))
    