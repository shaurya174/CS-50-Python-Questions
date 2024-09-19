str_input = input("Input: ")
str_output = ""
for i in str_input:
    IND = i.upper()
    if((IND=='A')or(IND=='E')or(IND=='I')or(IND=='O')or(IND=='U')):
        str_output+=""
    else:
        str_output+=i
print("Output:",str_output)