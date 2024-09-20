import random
def get_level():
    while True:
        level = input("Level: ")
        if(level=='1'or(level=='2')or(level=='3')):
            return int(level)
def generate_integer(level):
    integers = []
    if(level==1):
        integers.append(random.randint(0,9))
        integers.append(random.randint(0,9))
    elif(level==2):
        integers.append(random.randint(10,99))
        integers.append(random.randint(10,99))
    elif(level==3):
        integers.append(random.randint(100,999))
        integers.append(random.randint(100,999))
    return integers
user_level = get_level()
score = 0
for i in range(0,10):
    integers = generate_integer(user_level)
    act_ans = integers[0]+integers[1]
    wrong_count = 0
    user_ans = input(str(integers[0])+" + "+str(integers[1])+" = ")
    if(user_ans==str(act_ans)):
        score+=1
        continue
    else:
        wrong_count+=1
        print("EEE")
        while True:
            if(wrong_count==3):
                print(str(integers[0])+" + "+str(integers[1])+" = "+str(act_ans))
                break
            user_ans = input(str(integers[0])+" + "+str(integers[1])+" = ")
            if(user_ans==str(act_ans)):
               score+=1
               break
            wrong_count+=1
            print("EEE")
print("Score: ",score)
