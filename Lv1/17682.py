def solution(dartResult):
    answer = 0
    a = 0
    a2 = 0
    flag = False
    s = []
    dartResult = list(dartResult)
    for i in dartResult:
        if i == 'S':
            flag = False
            a = s.pop()
            s.append(a)
        elif i == 'D':
            flag = False
            a = s.pop()
            s.append(a*a)
        elif i == 'T':
            flag = False
            a = s.pop()
            s.append(a*a*a)
        elif i == '*':
            flag = False
            if len(s)>1:
                a = s.pop()
                a2 = s.pop()
                s.append(a2*2)
                s.append(a*2)
            else:
                a = s.pop()
                s.append(a*2)
        elif i == '#':
            flag = False
            a = s.pop()
            s.append(a*(-1))
        else:
            if flag == True:
                a = s.pop()*10 + int(i)
                s.append(a)
            else:
                a = int(i)
                s.append(a)
            flag = True
    answer = sum(s)
    return answer