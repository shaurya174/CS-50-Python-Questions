expression = input("Expression: ")
a = expression[0]
b=expression[4]
op = expression[2]
if(op=="+"):
    print(float(a)+float(b))
elif(op=="-"):
    print(float(a)-float(b))
elif(op=="*"):
    print(float(a)*float(b))
elif(op=="/"):
    print(float(a)/float(b))