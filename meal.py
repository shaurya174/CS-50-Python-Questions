user_time = input("What time is it? ")
def convert(time):
    to_return = 0.0
    hour_ind = time.find(":")
    to_return = (float(time[(hour_ind+1):])/60) + float(time[0:hour_ind])
    return to_return
exact_time = convert(user_time)
if((exact_time>=7.00)and(exact_time<=8.00)):
    print("breakfast time")
elif((exact_time>=12.00)and(exact_time<=13.00)):
    print("lunch time")
elif((exact_time>=18.00)and(exact_time<=19.00)):
    print("dinner time")