s = input("enter the string: ")
sub_string = input("enter the sub_string")
i = s.find(sub_string)
if i == -1:
	print("substring not found")
while i != -1:
	print("{} present at the index {}".format(sub_string,i))
	i = s.find(sub_string,i+len(sub_string),len(s))