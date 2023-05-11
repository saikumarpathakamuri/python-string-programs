kk = "saikumarpathakamuri"
lst=[]
for c in kk:
	if c not in lst:
		lst.append(c)
print(lst)
for i in lst:
	print(i ,"occurs ",kk.count(i)," times")

dic={}
for i in kk:
	if i not in dic:
		dic[i]=dic.get(i,0)+1
	else:
		dic[i]=dic[i]+1
print(dic)

for i,j in dic.items():
	print(i," occurs ",j," times")

d={}
for i in kk:
	if i not in d:
		d[i]=1
	else:
		d[i]=d[i]+1
print(d)
for i,j in d.items():
	print(i,j)


s=set(kk)
for i in sorted(s):
	print(i,kk.count(i))