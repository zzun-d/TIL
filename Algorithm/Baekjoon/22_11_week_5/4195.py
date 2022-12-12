import sys

def find(s):
    while type(friends[s]) == str:
        s = friends[s]
    return s


def input():
    return sys.stdin.readline().rstrip()


T = int(input())
for _ in range(T):
    F = int(input())
    friends = {}
    for _ in range(F):
        a, b = input().split()
        if friends.get(a):
            if type(friends[a]) == str:
                if friends.get(b):
                    if type(friends[b]) == str:
                        tmp_a = find(a)
                        tmp_b = find(b)
                        if tmp_a == tmp_b:
                            print(friends[tmp_a])
                            continue
                        friends[tmp_b] += friends[tmp_a]
                        friends[tmp_a] = tmp_b

                    elif type(friends[b]) == int:
                        tmp_a = find(a)
                        if tmp_a == b:
                            print(friends[b])
                            continue
                        friends[b] += friends[tmp_a]
                        friends[tmp_a] = b
                else:
                    tmp_a = find(a)
                    friends[b] = tmp_a
                    friends[tmp_a] += 1

            elif type(friends[a]) == int:
                if friends.get(b):
                    if type(friends[b]) == str:
                        tmp_b = find(b)
                        if tmp_b == a:
                            print(friends[a])
                            continue
                        friends[a] += friends[tmp_b]
                        friends[tmp_b] = a
                        
                    elif type(friends[b]) == int:
                        friends[a] += friends[b]
                        friends[b] = a
                else:
                    friends[a] += 1
                    friends[b] = a

        elif friends.get(b):
            if type(friends[b]) == str:
                tmp = find(b)
                friends[a] = tmp
                friends[tmp] += 1

            elif type(friends[b]) == int:
                friends[a] = b
                friends[b] += 1


        else:
            friends[a] = 2
            friends[b] = a
        print(friends[find(a)])
