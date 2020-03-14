def solution(arr):
    temp = sorted(arr)
    arr.remove(temp[0])
    if len(arr)==0:
        arr.append(-1)
    return arr