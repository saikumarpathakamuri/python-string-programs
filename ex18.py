s = "ABCABCABCA"
sub_string = "ABC"

i = s.find(sub_string)
print(sub_string,"present at the index ",i)
i = s.find(sub_string,i+len(sub_string),len(s))
print(sub_string,"present at the index ",i)
i = s.find(sub_string,i+len(sub_string),len(s))
print(sub_string,"present at the index ",i)