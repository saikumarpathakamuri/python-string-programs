word= "saikumar".lower()
vowels="a,e,i,o,u"
d={}

for ch in word:
	if ch in vowels:
		d[ch]=d.get(ch,0)+1
print(d)
