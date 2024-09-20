products = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
total = 0
while True:
    item = input("Item: ")
    if(item==""):
        print("Total: $"+str(total))
        break
    for i in products.keys():
        if((i.lower())==(item.lower())):
            total+=products[i]
            print("Total: $"+str(total))


    
