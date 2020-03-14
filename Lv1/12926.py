def solution(s, n):
    
    answer = ''
    for i in range(len(s)):
        if ord(s[i])==32:
            answer += ' '           
        elif ord(s[i]) < 91:
            d = (ord(s[i])+n-65)%26+65 
            answer += chr(d)
        else:
            d = (ord(s[i])+n-97)%26+97
            answer += chr(d)
            
    print(answer)    
    return answer