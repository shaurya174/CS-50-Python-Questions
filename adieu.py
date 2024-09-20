names = []
while True:
    name = input("Name: ")
    if(name==""):
        break
    names.append(name)
if(len(names)==1):
    print("Adieu,adieu,to "+names[0])
elif(len(names)==2):
    print("Adieu,adieu,to "+names[0]+ " and "+names[len(names)-1])
else:
    to_print="Adieu,adieu,to "+names[0]
    for i in range(1,len(names)-1):
        to_print = to_print + ", "+names[i]
    to_print = to_print + " and "+names[len(names)-1]
    print(to_print)

    