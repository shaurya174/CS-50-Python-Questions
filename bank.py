test_string = input("Greeting: ")
test_string = test_string.lower()
if(test_string.startswith("hello")):
    print("$0")
elif(test_string.startswith("h")):
    print("$20")
else:
    print("$100")