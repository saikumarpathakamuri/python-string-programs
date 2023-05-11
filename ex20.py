s = "SAISAISAISAIA"
sub_string = "SAI"
i = s.find(sub_string)
count = 0
if i == -1:
	print("substring not found")
while i != -1:
	count = count+1
	print("{} present at the index {}".format(sub_string,i))
	i = s.find(sub_string,i+len(sub_string),len(s))

print("{} count of the substring is  : {}".format(sub_string,count))

print(sub_string,"count of the substring is ",s.count(sub_string))