# 2의 배수 집합으로 표현
multi_2 = set([i for i in range(2, 1000, 2)])

# 7의 배수 집합으로 표현
multi_7 = set([i for i in range(7, 1000, 7)])

# 2의 배수, 7의 배수 합집합
multi_2_7 = multi_2 | multi_7

# 합집합 원소 모두 더하기
print(sum(multi_2_7))
