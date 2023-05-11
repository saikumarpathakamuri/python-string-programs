a="ABAABBCA"
d="".join(sorted(a))
kes=""
c=1
pre=d[0]
i=1
while i<len(d):
	if d[i]==pre:
		c=c+1
	else:
		kes=kes+str(c)+pre
		pre=d[i]
		c=1
	if i==len(d)-1:
		kes=kes+str(c)+pre
	i=i+1
print(kes)