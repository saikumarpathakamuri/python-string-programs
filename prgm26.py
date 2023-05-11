a="abcdefg"
b="xyz"
c="12345"

kk=""
i,j,k=0,0,0

while i<len(a) or j<len(b) or k<len(c):
	if i<len(a):
		kk=kk+a[i]
		i+=1
	if j<len(b):
		kk=kk+b[j]
		j+=1
	if k<len(c):
		kk=kk+c[k]
		k=k+1
print(kk)