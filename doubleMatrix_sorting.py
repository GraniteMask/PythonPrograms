l=[]
h=[]
p=[]
f=[]
n=int(input())
for i in range(n):
    l.append(int(input()))
    h.append(int(input()))
for i in range(n):
    p.append(h[i])
for i in range(n):
    for j in range(n-i-1):
        if h[j]>h[j+1]:
            temp=h[j]
            h[j]=h[j+1]
            h[j+1]=temp
for i in range(n):
    for j in range(n):
        if h[i]==p[j]:
            f.append(l[j])
print(f)