A = 'banana'
B = 'ana'
s = A+'1'+B
n = len(s)

suffix = [i for i in range(n)]
g = [0]*(n+1)
ng = [0]*(n+1)

for i in range(n):
    g[i]=ord(s[i])

g[n]=-1
ng[suffix[0]]=0
ng[n]=-1

print('suffix',suffix)
print('g',g)
print('ng',ng)


t = 1

while t<n:
    suffix.sort(key=lambda x:g[x],g[min(x+t,n)])
    if ng[n-1]==n-1:
        break