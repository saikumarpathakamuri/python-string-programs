s1 = "Sandesh"
s2 = "Suhas"
res = ""
i,j=0,0
while i<len(s1) or i<len(s2):
	if i<len(s1):
		res=res+s1[i]
	if j<len(s2):
		res=res+s2[i]
	i=i+1
	j=j+1
print(res)