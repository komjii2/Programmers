import math as m

def solution(n):
    answer = -1
    size = int(m.sqrt(n))
    if size*size == n:
        answer = (size+1)*(size+1)
        
        
    
    return answer