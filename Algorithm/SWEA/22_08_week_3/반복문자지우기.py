T = int(input())
for t in range(1, T+1):
    s = input()
    while True:
        i = 0
        old_l = len(s)                  # 처리 전 문자열 길이 저장
        while len(s) > i+1:             # 인덱스 에러 방지
            if s[i] == s[i+1]:              # 반복문자 제거 인덱싱
                s = s[:i] + s[i+2:]
                if i > 0:
                    i -= 1                      # index 갱신(짧아진 s 반영)
                continue
            i += 1
        if old_l == len(s):             # 처리 전, 후 문자열 길이 변화 없으면 break
            break
    print(f'#{t} {len(s)}')