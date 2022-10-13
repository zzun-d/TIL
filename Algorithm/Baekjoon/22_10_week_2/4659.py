import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    prob = input()
    
    if prob == 'end':
        break

    S = list(prob)
    moum = ['a', 'e', 'i', 'o', 'u']
    if set(S).intersection(set(moum)):
        stack = [S.pop()]
        finish = False

        if stack[0] in moum:
            tmp = True
        else:
            tmp = False
        
        while S:
            s = S.pop()
            if tmp:
                if s in moum:
                    stack.append(s)
                else:
                    stack = [s]
                    tmp = False
            else:
                if s not in moum:
                    stack.append(s)
                else:
                    stack = [s]
                    tmp = True
            
            if len(stack) == 2 and stack[-2] == stack[-1] and stack[-1] not in moum:
                print(f'<' + prob + '> is not acceptable.')
                finish = True
                break
            
            elif len(stack) > 2:
                print(f'<' + prob + '> is not acceptable.')
                finish = True
                break
        
        if not finish:
            print(f'<' + prob + '> is acceptable.')
    
    else:
        print(f'<' + prob + '> is not acceptable.')
