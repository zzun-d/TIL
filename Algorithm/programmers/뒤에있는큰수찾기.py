def solution(numbers):
    answer = [-1]
    nums = [numbers[-1]]
    for i in range(len(numbers)-2, -1, -1):
        
        while nums and nums[-1] <= numbers[i]:
            nums.pop()
        
        else:
            if nums:
                answer.append(nums[-1])
            else:
                answer.append(-1)
        nums.append(numbers[i])
        
    answer.reverse()
    return answer

