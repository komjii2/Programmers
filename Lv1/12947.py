def solution(x):
    answer = True
    div = 0
    a = x
    while x > 0:
        div = div + int(x%10)
        x = int(x/10)
    
    if a % div !=0:
        answer=False
    return answer