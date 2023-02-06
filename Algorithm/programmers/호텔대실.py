import heapq

def solution(book_time):
    answer = 0
    lst_s = []
    lst_e = []
    cnt = 0
    for s_t, e_t in book_time:
        sh, sm = s_t.split(':')
        eh, em = e_t.split(':')
        s = int(sh)*60 + int(sm)
        e = int(eh)*60 + int(em) + 10
        heapq.heappush(lst_s, (s, e))
    for _ in range(len(lst_s)):
        s, e = heapq.heappop(lst_s)
        heapq.heappush(lst_e, e)
        while s >= lst_e[0]:
            heapq.heappop(lst_e)
            cnt -= 1
        cnt += 1
        if answer < cnt:
            answer = cnt
        
    return answer