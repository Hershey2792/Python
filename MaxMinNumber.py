# author: Quentin Jefferies
# date: 2/7/21 

maximum = 0
minimum = 0

#loop through 4 numbers and receive input
try:
    for i in range(4):
        num = float(input('Enter a number: '))

        if maximum is 0:# if max or min is 0 then its automatically min
            maximum = num

        if num > maximum:# each number greater than 0 is assigned max
            maximum = num
        
        elif num < maximum:# each number less than the next is assigned min
            minimum = num


except:
    print 'You did not enter a number, the program will quit'
    quit()

print 'The maximum number is:', maximum
print 'The minimum number is:', minimum