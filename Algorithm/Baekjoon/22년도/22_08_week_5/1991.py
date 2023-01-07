def tree_1(root):
    if root != '.':
        print(root, end='')
        tree_1(tree[root][0])
        tree_1(tree[root][1])

def tree_2(root):
    if root != '.':
        tree_2(tree[root][0])
        print(root, end='')
        tree_2(tree[root][1])

def tree_3(root):
    if root != '.':
        tree_3(tree[root][0])
        tree_3(tree[root][1])
        print(root, end='')

N = int(input())
tree = {i[0]:[i[1], i[2]] for i in [list(input().split()) for _ in range(N)]}

tree_1('A')
print()
tree_2('A')
print()
tree_3('A')