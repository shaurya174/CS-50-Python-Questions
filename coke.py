total_amount = 50
get_amount = 0
while True:
    print("Amount Due:",total_amount)
    coin = int(input("Insert Coin: "))
    if((coin==25)or(coin==10)or(coin==5)):
        total_amount=total_amount-coin
    if(total_amount<=0):
        print("Change Owed:",(-(total_amount)))
        break
