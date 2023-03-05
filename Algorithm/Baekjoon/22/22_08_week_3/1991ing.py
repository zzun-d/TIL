N = int(input())
nodes = [input().split() for _ in range(N)]
node_dict = {node[0]:[node[1], node[2]] for node in nodes}
stack = []
pront = []
middle = []
back = []

while stack:
    if node_dict[stack.pop()][1] != '.':
        