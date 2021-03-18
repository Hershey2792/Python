#Quentin Jefferies
#Hw4 Lists
#CMSC 206
#2/24/21



#ask user for three first names 
first = []
last = []
fullname = []

#Put names ina list using getNames function
def getNames(first, last, fullname):
    for i in range(3):
        first.append(raw_input('Enter first name: '))
        last.append(raw_input('Enter last name: '))
        first_Full = first[i], last[i]
        fullname.append(first_Full)
          
    print 'First name: ', first 
    print 'last name:   ', last
    print 'Full name: ', fullname
    
    #get specific row and column from user
    print '\nSELECT the row and column you want'
    row = int(input('enter row (0 - 2): '))
    column = int(input('enter column (0 - 2): '))

    if row is 0 or column is 0:
        print fullname[0]  

    elif row is 1 or column is 1:
        print fullname[1]

    elif row is 2 or column is 2:
        print fullname[2]
    
    else:
        print 'The column doesnt exist'
            
#Call the function    
getNames(first, last, fullname)

