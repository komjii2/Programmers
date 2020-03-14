from collections import Counter as C

def solution(participant, completion):
    answer = ''
    C_p = C(participant)
    C_c = C(completion)
    C_a = C_p - C_c
    
    for k,v in C_a.items():
        if v != 0:
            answer = k
        
    
    return answer