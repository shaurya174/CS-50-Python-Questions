dictt = {}
while True:
    item = input("")
    if(item ==""):
        break
    if((item.upper()) in dictt.keys()):
        dictt[item.upper()]+=1
    else:
        dictt[item.upper()] = 1
for i in dictt.keys():
    print(str(dictt[i])+" "+i)