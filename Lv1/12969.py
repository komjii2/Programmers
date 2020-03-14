a, b = map(int, input().strip().split(' '))

for i in range(b):
    s = ''
    for i in range(a):
        s += "*"
    print(s)