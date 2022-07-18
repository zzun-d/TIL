score = {
    'python' : 80,
    'django' : 89,
    'web' : 83
}

# 1. 신규 과목 'algorithm' 90점 획득 socre에 추가하기
score['algorithm'] = 90

# 2. python 과목 점수 80 -> 85로 정정 score에서 수정하기
score['python'] = 85

# 3. 김해피의 전체 과목 평균 점수 출력하기
print(sum(list(score.values()))/len(score))