def solution(storey):
    answer = 0
    lst = list(map(int, list(str(storey))))
    plus = 0
    
    while lst:
        n = lst.pop()
        n += plus
        if n > 5 or (lst and n == 5 and lst[-1] >= 5):
            answer += 10 - n
            plus = 1
        else:
            answer += n
            plus = 0
        print(answer)
    if n > 5:
        answer += 1
            
                
    return answer
