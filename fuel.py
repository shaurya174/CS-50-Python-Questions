while True:
    fraction = input("Fraction: ")
    slash_index = fraction.find("/")
    try:
        a = float(fraction[0:slash_index])
        b = float(fraction[(slash_index+1):])
        c = (a/b)
        c = c*100
        c = int(c)
        if(c>=99):
            print("F")
            break
        elif(c<=1):
            print("E")
            break
        else:
            print(str(c)+"%")
            break
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
        