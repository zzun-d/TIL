import sys
from collections import deque, defaultdict
def input():
    return sys.stdin.readline().rstrip()


n = input()
lst = []
tree = defaultdict(list)
while n != '':
    lst.append(n)
    n = input()
lst = deque(list(map(int, lst)))
stack = [lst.popleft()]
while True:
    n = lst.popleft()
    if stack[-1] > n:
        tree[stack[-1]].append(n)
        stack.append(n)
    else:
        while stack:
            stack.pop()
            if stack[-1] > n:








class Node:
    def __init__(self, root, left, right):
        self.root = root
        self.left = left
        self.right = right

