def solution(s):
    answer = True
    if len(s) == 4 or len(s) ==6:
        s = list(s)
        for i in s:
            if not i.isdigit():
                answer = False
                break
    else:
        answer = False
    
    
    return answer