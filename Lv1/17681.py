def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        ans = format(arr1[i]|arr2[i],'b')
        for j in range(n-len(ans)):
            ans = '0'+ans
        ans = ans.replace("1","#")
        ans = ans.replace("0"," ")        

        answer.append(ans)
    
    
    return answer