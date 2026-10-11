def solution(num_list):
    answer = 1
    if len(num_list) >= 11:
        answer = 0
        for n in num_list:
            answer += n
    else:
        for n in num_list:
            answer *= n
    return answer