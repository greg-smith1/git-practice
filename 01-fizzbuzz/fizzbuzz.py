reps = input()
reps = int(reps)
    
buzz = ['Fizz' if i%3==0 else 'Buzz' if i%5==0 else 'FizzBuzz' if (i%3==0 and i%5==0) else i for i in range(0, reps)]
print (buzz)