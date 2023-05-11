s = "sandesh"
for mm in s:
	print(mm)
i = 0
l = len(s)
k = []
j = []
print(s)
for m in s:
	if i % 2 ==0 :
		k.append(m)
	else:
		j.append(m)
	i=i+1

print(k)
print("even index is :","".join(k))
print("odd index is :","".join(j))