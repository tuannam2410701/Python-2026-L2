number = int (input('Enter a number? '))
total = 0
for i in range(1,number):
    if number % i == 0:
        total = total + i
        print(total)
if total == number:
    print(f'{number} is a perfect number')
else:
    print(f'{number} is not a perfect number')