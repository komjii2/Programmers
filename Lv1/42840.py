def solution(answers):
    answer = [0,0,0]
    res = []
    s_1 = [1, 2, 3, 4, 5]
    s_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    s_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    len_s1 = len(s_1)
    len_s2 = len(s_2)
    len_s3 = len(s_3)
    
    for i in range(len(answers)):
        if s_1[i%len_s1] == answers[i]:
            answer[0] = answer[0] +1
        if s_2[i%len_s2] == answers[i]:
            answer[1] = answer[1] +1
        if s_3[i%len_s3] == answers[i]:
            answer[2] = answer[2] +1
    
    flag = answer.count(max(answer))
    
    for i in range(flag):
        res.append(answer.index(max(answer))+i+1)
        answer.pop(answer.index(max(answer)))
        
    return res