def Loop(num):
    if num % 3 == 0:
        print("fizz")
    if num % 5 == 0:
        print("Buzz")
    elif num % 3 == 0 and num % 5 ==0:
        print("'FizzBuzz'")
    

Loop(8)
Loop(10)
Loop(9)