num = []

for i in range(9):
    num.append(int(input()))

cnt = 0
max = 0

for i,j in enumerate(num):

    if j > max:
        max = j
        cnt = i

print(max)
print(cnt+1)