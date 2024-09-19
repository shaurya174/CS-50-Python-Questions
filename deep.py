test_string = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")
test_string = test_string.lower()
if((test_string=='42')or(test_string=='forty-two')or(test_string=='forty two')):
    print("Yes")
else:
    print("No")