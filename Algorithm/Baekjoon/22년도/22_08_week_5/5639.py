import sys
sys.setrecursionlimit(10**6)
def input():
    return sys.stdin.readline().rstrip()


n = input()
lst = []
while n != '':
    lst.append(int(n))
    n = input()

def tree(s, e):
    if s > e:
        return

    m = e
    for i in range(s+1, e+1):
        if lst[i] > lst[s]:
            m = i - 1
            break

    tree(s+1, m)
    tree(m+1, e)
    print(lst[s])

tree(0, len(lst)-1)