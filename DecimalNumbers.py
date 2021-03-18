# Author: Quentin Jefferies
# Number Converter Project1
# 2/3/21

# Menu
print('Number Converter -> convert a number (between 0 - 255) from\n')
print('Enter 1 -- Decimal to Hexadecimal')
print('Enter 2 -- Decimal to Octal')
print('Enter 3 -- Decimal to Binary (Between 0 and 64)')
print('Enter x -- Exit\n')

while True:
    choice = input('Enter your choice: ') # conditional based on choice X
    if choice == 'x':
        quit()

# conditional based on choice 1
    elif int(choice) == 1:
        x = int(input('Enter a decimal number: '))
        if x > 256:
            print('Invalid input value. Try again\n')
        else:
            print('Base-10:', x, ', Hex:', hex(x) + '\n')

# conditional based on choice 2
    elif int(choice) == 2:
        x = int(input('Enter a decimal number: '))
        if x > 256:
            print('Invalid input value. Please try again\n')
        else:
            print('Base-10:', x, ', Oct:', oct(x) + '\n')

# conditional based on choice 3
    elif int(choice) == 3:
        x = int(input('Enter a decimal number: '))
        if x > 64:
            print('Invalid input value. Please try again\n')
        else:
            print('Base-10', x, ',Bin:', bin(x) + '\n')

    else:
        print('Invalid input. Please try again')

