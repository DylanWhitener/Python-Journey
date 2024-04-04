def collatz(number):
    if number % 2 == 0: # returns if its a even number
        return number // 2
    else: # if not even it must be odd
        return 3 * number + 1

print('Enter Number: ')
while True: # main loop in case of error handling.
    try:
        num = int(input())
        if num <=0:
            raise ValueError('Number must be greater than 0')
        while num > 1:
            num = collatz(num)
            print(num)
        break # exits main loop once its done
    except ValueError:
        print('Please enter a valid int.')