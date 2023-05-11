s = "Sandesh"
i = 0
lst=[]
k=[]
while i<len(s):
	if i%2==0:
		lst.append(s[i])
	else:
		k.append(s[i])
	i = i+1

print("even index characters are : ","".join(lst))
print("odd index characters are : ","".join(k))


s="Sandesh"
print("even index characters are : ",s[::2])
print("odd index characters are : ",s[1::2])