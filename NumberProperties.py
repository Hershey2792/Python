
#sum, average and minimum function 
def numCalc(num):
    lst = []
    while num is not 0:
        for i in range(num):
            numbers = int(input('Enter numbers (press done to stop): '))
            lst.append(numbers)

        print '\nSum of the list of numbers is:', sum(lst)
        print 'The average of the list of numbers is:', float(sum(lst)/len(lst))
        print 'The minimum number of the list is:', min(lst),'\n'
        break


#create list and call calculation function
num = int(input('How many numbers do you want to enter: '))        
numCalc(num)

#prime function 
def is_prime(num):
    for i in range(2, num):
        if num % i == 0: #if number is divisible by any other number evenly within range it
            print 'This number is not prime'
            break
        
        else:
            print 'This number is prime'
            break
        

#call prime number function 
print 'Welcome to the prime calculation'
num = int(input('Enter a number: '))
is_prime(num)