# author: Quentin Jefferies
#date: 2/14/2021
# Project 2 
# first and final attempt

def ask_user():
    print('Which verse should I generate (Enter a number between 1 and 99)')



def beer_lyrics(num):
    try:
        while num > -1:
            if num > 100:
                print 'Invalid selection number\n'
                break

            if num > 1:
                print num, 'bottles of beer on the wall,'
                print num, 'bottles of beer,'
                print 'Take one down pass them around,'
                print num - 1, 'bottles of beer on the wall!\n'


            elif num is 1:
                print num, 'bottle of beer on the wall,'
                print num, 'bottle of beer,'
                print 'Take one down pass them around,'
                print 'No more bottles of beer on the wall!\n'
            
            elif num is 0:
                print 'No more bottles of beer on the wall'
                print 'No more bottles of beer,'
                print 'Go to the store and buy some more,'
                print '99 bottles of beer on the wall!\n'
                break
            
            num -= 1

    except:
        print 'invalid selection'

while True:
    ask_user()
    num = int(input('Enter a number: '))
    beer_lyrics(num)
    result = int(input('Would you like to repeat?(Enter 1 or 0): '))
    if result is 1:
        continue

    elif result is 0:
        break

