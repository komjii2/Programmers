def solution(n, lost, reserve):
    s =[]
    answer = 0
    lost = set(lost)
    reserve = set(reserve)
    for i in range(n+2):
        s.append(1)
        if i in lost:
            s[i] -= 1
        if i in reserve:
            s[i] += 1

    for i in range(1,n):
        if s[i] == 0 and s[i-1] ==2:
            s[i] += 1
            s[i-1] -= 1
        elif s[i] == 0 and s[i+1] ==2:
            s[i] += 1
            s[i+1] -= 1
    
    for i in range(n+2):
        if s[i] > 0:
            answer += 1
    answer -= 2        
    
    return answer