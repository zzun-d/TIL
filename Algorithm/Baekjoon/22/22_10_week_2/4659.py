import sys

def input():
    return sys.stdin.readline().rstrip()

while True:
    prob = input()
    
    if prob == 'end':
        break
    
    S = list(prob)
    moum = ['a', 'e', 'i', 'o', 'u']

    if not set(S).intersection(set(moum)):      # 주어진 문자열에 모음 유무
        finish = True

    else:
        finish = False
        stack = [S.pop()]
        
        if stack[0] in moum:                    # 모음이면 tmp true
            tmp = True
        else:                                   # 자음이면 tmp False
            tmp = False
        
        while S:                                # 문자열 남았으면 계속
            s = S.pop()                         # 다음 문자 확인
            if tmp:                             # 모음이었을 경우
                if s in moum:
                    stack.append(s)
                else:
                    stack = [s]
                    tmp = False
            else:                               # 자음이었을 경우
                if s not in moum:
                    stack.append(s)
                else:
                    stack = [s]
                    tmp = True
            if len(stack) == 2 and stack[-1] == stack[-2]:      # 쌓인 모음이나 자음의 길이가 2고 두개가 모두 같으면사
                if stack[-1] not in ['e', 'o']:                 # 해당 글자가 e, o가 아니면 불가
                    finish = True
                    break
            elif len(stack) > 2:                                # 쌓인 글자가 3개 이상이면 불가
                finish = True
                break
        
    if not finish:
        print(f'<{prob}> is acceptable.')
    else:
        print(f'<{prob}> is not acceptable.')
