test_string = input("camelCase: ")
snake_case=""
cap_index = -1
for i in test_string:
    if(i.islower()):
        snake_case+=i
    elif(i.isupper()):
        snake_case = snake_case+"_"+(i.lower())
    else:
        snake_case+=i
print("snake_case:",snake_case)

