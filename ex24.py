s = "python is a leading programming language"
print(s)
new_string = s.split()
print(new_string)
for i in new_string:
	print(i)

date = "3-11-2022"
date = date.split("-")
print(date)
for i in date:
	print(i)
a = "earth,moon,sun,stars"
a = a.split(",")
print(a)
a = "earth,moon,sun,stars"
a = a.split(",",maxsplit=2)
print(a)
s = "python is a leading programming language"
print(s.split("/"))

s = "python is a leading programming language"
print(s.split(" "))