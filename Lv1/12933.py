def solution(n):
    answer = []
    size = 0
    while n > 0:
        answer.append(n%10)
        n = int(n/10)
    
    answer.sort(reverse = True)
    
    for i in answer:
        size = size * 10 + i
    
    return size