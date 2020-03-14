import math as f

def lcm(a, b):
    gcd_value = f.gcd(a, b)
    if (gcd_value == 0): 
        return 0
    return abs( (a * b) / gcd_value )

def solution(n, m):
    answer = []
    answer.append(f.gcd(n,m))
    answer.append(lcm(n,m))
    return answer