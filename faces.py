def convert(test_string):
    if((test_string.find(":)"))!=(-1)):
        test_string=test_string.replace(":)","🙂")
    if((test_string.find(":("))!=(-1)):
        test_string=test_string.replace(":(","🙁")
    return test_string
test_string = input("")
test_string=convert(test_string)
print(test_string)
