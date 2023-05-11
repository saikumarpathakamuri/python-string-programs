a="ABAABBCA"
s="".join(sorted(a))
l=""
k=1
pre=s[0]
ll=1
while ll<len(s):
	if s[ll]==pre:
		k=k+1
	else:
		l=l+str(k)+pre
		pre=s[ll]
		k=1
	if ll==len(s)-1:
		l=l+str(k)+pre

	ll=ll+1

print(l)