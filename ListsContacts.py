#create an array of contacts 
name = []
phone = []
email = []

#create a function to add contacts to the list of contacts
def addContact():
while True:
    addName = input('Enter a name: '):
    name.append(addName);

    addPhone = raw_input('Enter a phone: ')
    name.append(addPhone);

    addEmail = input('Enter a email:    ')
    name.append(addEmail);
    break

#create a function with main menu option 
def main():
    Print 'What would you like to do? Enter a number 1 - 5: '
    Print '1. Add entry'
    Print '2. Update entry'
    Print '3. Delete entry'
    Print '4. Look up an entry'
    Print '5. Quit'


##Update entry 
