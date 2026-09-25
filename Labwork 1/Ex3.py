number = int (input('Enter a number? '))
isPrime = 1
if number <= 1:
    isPrime = 0
elif number == 2:
    isPrime = 1
else:
    for i in range(2,number):
        if number % i != 0:
            isPrime = 0
if isPrime:
    print("Prime")
else:
    print("Not")