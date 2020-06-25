def currency_converter(amount):

    amount_float= float(amount)
    cents= round(amount_float*100)
    hundreds= cents//10000
    cents=cents%10000
    fifties= cents//5000
    cents=cents%5000
    twenties=cents//2000
    cents=cents%2000
    tens=cents//1000
    cents=cents%1000
    fives=cents//500
    cents=cents%500
    ones=cents//100
    cents=cents%100
    quarters=cents//25
    cents=cents%25
    dimes=cents//10
    cents=cents%10
    nickels=cents//5
    cents=cents%5
    pennies=cents
    print("You have:")
    if hundreds!=0:
        print(str(hundreds)+" $100")
    if fifties !=0:
        print(str(fifties)+" $50")
    if fifties !=0:
        print(str(twenties)+" $20")
    if tens!=0:
        print(str(tens)+" $10")
    if fives!=0:
        print(str(fives)+" $5")
    if ones!=0:
        print(str(ones)+" $1")
    if quarters!=0:
        print(str(quarters)+" quarter")
    if dimes !=0:
        print(str(dimes)+" dime")
    if nickels!=0:
        print(str(nickels)+" nickel")
    if pennies!=0:    
        print(str(pennies)+" penny")


#currency_converter(12.33)

