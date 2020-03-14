def solution(strings, n):
    answer = []
    d = {i[n] : [] for i in strings}
    print(d)
    for s in strings:
        d[s[n]].append(s)

    for k in d.keys():
        d[k].sort()
    d = sorted(d.items())
    print(d)
    for i in d:
        for j in i[1]:
            answer.append(j)
    print(answer)
    return answer