def solution(a, b):
    total = 0
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    
    for i in range(a-1):
        total += month[i]
    total += b
    answer = day[total%7]
    return answer