a, b = map(int, input().split())

if a == 0:
    a = 24

if b < 45:
    a = a - 1
    b = 60 - 45 + b
else:
    if a == 24:
        a = 0
    b = b - 45
print(a,b)