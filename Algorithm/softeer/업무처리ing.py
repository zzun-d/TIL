from collections import deque

H, K, R = map(int, input().split())
tree = [[deque([]), deque([])] for _ in range(2**(H+1))]
n = 1

for i in range((2**(H+1))//2, 2**(H+1)):
    tree[i][0] = deque(list(map(int, input().split())))

def confirm():
    for i in range(1, 2**(H)):
        if i % 2:
            tree[i//2][1 if i % 2 == 1 else 0].append(tree[i][0 if n%2 == 1 else 1])

def working():
    for i in range(2, 2**(H+1)):
        child = 1 if i % 2 else 0
        if tree[i][child]:
            tree[i//2][child].append(tree[i][child].popleft())
    

for _ in range(R):
    confirm()
    working()
    n += 1

print(tree[0])


