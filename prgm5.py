s = "Sandesh is a Very Good Chess player"
s=s.split()
k=0
lst=[]
for i in s:
	if k%2==0:
		lst.append(i)
	else:
		lst.append(i[::-1])
	k=k+1
print(" ".join(lst))