N,K=map(int,input().split())
H=list(map(int,input().split()))
h=[]
r=0
for i in range(1,N):
    h.append(H[i]-H[i-1])
h.sort()
print(sum(h[:N-K]))
