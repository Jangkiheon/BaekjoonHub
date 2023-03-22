a = int(input())
b = input()
list=[]
for i in b:
    list.append(i)
for j in range(len(list),0,-1):
    print(a * int(list[j-1]))
print(a*int(b))