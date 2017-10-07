
##Andrew Baldwin

##Do I get points off for using global database in each function?
###Just wanted to make sure it was always grabbing the full database

def welcome():
    '''
Prints a simple welcome message. No parameters of returns.
    '''
    print('''
---------------------------------------------------------------------------\n
Welcome to this the CISC106 Database System. This program allows the user to\n
interact simply with files in a database. Here, the user can create, modify,\n
and maintain a simple database.\n
---------------------------------------------------------------------------
    ''')

    
def menu():
    '''
Prints a menu with a list of database functions. No parameters or returns.
    '''
    print('''
--------------------------------Main Menu------------------------------\n
Database functions:  \n
    d - delete record  \n
    f - find record  \n
    i - insert record  \n
    p - print database  \n
    r - read and merge  \n
    q - query grades and sections  \n
    c - chart grades in pie chart  \n
    e - exit program  \n
-----------------------------------------------------------------------
    ''')

    
def bye():
    '''
Prints a simple goodbye message. No parameters or returns.
    '''
    print('Exiting program, goodbye')


def delete():
    '''
Searches the database for a record using an inputed last name.
If it exists it is deleted, if not an error message is returned.
No parameters or returns.
    '''
    #Establishes list to be used for removal
    data = []
    check = 0
    global full_database
    name = input("What is the last name of the record you'd like to delete?")
    #Searches for record and grabs the data from it if it is there
    for record in range(len(full_database)):
        #Checking last names
        x = full_database[record][1]
        #Matching given name to last names
        if name == x:
            check = check + 1
            data = full_database[record]
    #Validation check
    if check >= 1:
        #Removes saved data
        full_database.remove(data)
        print('Record has been deleted.')
    else:
        print('Record does not exist.')

        
def find_record():
    '''
Searches the database for a record using a last name,
and if it exists, prints it.
No parameters or returns.
    '''
    global full_database
    check = 0
    name = input("What is the last name of the record you'd like to find?")
    #Searches for record and prints it if it is there
    for record in range(len(full_database)):
        #Checking last names
        x = full_database[record][1]
        #Matching given name to last names
        if name == x:
            check = check + 1
            print(full_database[record])
    #When record is not there
    if check < 1: 
        print('Record does not exist.')


def insert_record():
    '''
Inserts a record into the database if it does not already
exist. Also tests to make sure given values are within the databases'
parameters. Makes sure to resort database. No parameters or returns.
    '''
    global full_database
    #Temporary list variables for sorting
    sort_list = []
    last_names = []
    #Empty list for new data
    new = []
    first_name = input('What is the first name?')
    last_name = input('What is the last name?')
    #Validation testing
    for record in full_database:
        #Checks against other last names
        if last_name == record[1]:
            print('Last name already in database.')
            last_name = input('Please reenter a last name:')
    sect_num = int(input('What is the section number?'))
    #Checks that given section number is within limits
    while sect_num < 40 or sect_num > 43:
        print('Invalid section number, try again.')
        sect_num = int(input('Reenter a section number:'))
    grade = float(input('What is their grade?'))
    #Checks that givin grade is within limits
    while grade < 0 or grade > 100:
        print('Invalid grade input.')
        grade = float(input('Please reenter their grade:'))
    #Adds values to new data list    
    new.append(first_name)
    new.append(last_name)
    new.append(sect_num)
    new.append(grade)
    #Puts given name into list for sorting
    last_names.append(new[1])
    #Grabs all last names
    for records in full_database:
        last_names.append(records[1])
    #Resorts last names
    list_sort(last_names)
    #Puts all new data into database
    full_database.append(new)
    #Resorts all data into sort_list using last name list
    for name in last_names:
        for record in range(len(full_database)):
            b = full_database[record][1]
            if name == b:
                sort_list.append(full_database[record])
    #Resets the database to the sorted version
    full_database = sort_list
    print('The record', new , 'has been successfully inserted.')

            

def print_database():
    '''
Prints the database line by line.
No parameters or returns.
    '''
    global full_database
    print()
    for record in full_database:
        print(record)
    print()


def read_and_merge():
    '''
Opens and reads two files given by the user and creates a
database from each one. Then prints the content of each
database line by line, then closes the files.
File names are inputted by user.
No parameters or returns.
    '''
    #To help stop this from being run more than once
    global Extra
    Extra = Extra + 1
    #Establishes empty temporary lists
    sorted_list = []
    last_names = []
    #creates the central database variable
    global full_database
    full_database = []
    #Gets first file
    file1 = str(input('What is the name of the first file?'))
    file1= open(file1, 'r')
    #Gets second file
    file2 = str(input('What is the name of the second file?'))
    file2= open(file2, 'r')
    #Reads the first line of the first file
    line1 = file1.readline()
    #Reads every other line, stops when it gets to the end
    while line1 != '':
        #Prepares lines for database
        line1 = line1.rstrip('\n')
        line1 = line1.split(" ")
        line1[2] = int(line1[2])
        line1[3] = float(line1[3])
        #Adds each line to the database
        full_database.append(line1)
        #Moves to the next line
        line1 = file1.readline()
    #Reads the first line of the second file
    line2 = file2.readline()
    #Reads every other line, stops when it gets to the end
    while line2 != '':
        #Prepares lines for database
        line2 = line2.rstrip('\n')
        line2 = line2.split(" ")
        line2[2] = int(line2[2])
        line2[3] = float(line2[3])
        full_database.append(line2)
        #Moves to the next line
        line2 = file2.readline()
    #Gets just the last names
    for name in full_database:
        last_names.append(name[1])
    #Sorts the last names
    list_sort(last_names)
    #Nested for loop that organizes the records into sorted_list
    ##Using the last_names list
    for name in last_names:
        for record in range(len(full_database)):
            match = full_database[record][1]
            if name == match:
                sorted_list.append(full_database[record])
    #Resets original database to the organized one
    full_database = sorted_list
    #Closing time
    file1.close()
    file2.close()
    print('The files have been read and merged together.')


def list_sort(List):
    '''
    Parameters:
         List (list) - List of unsorted stuff

    Returns:
         Sorted list (list) - List that is sorted
    '''
    #Goes through every value in the list
    for index in range(1,len(List)):
        value = List[index]
        i = index-1
        while i>=0: #Loops until done
            if value < List[i]:
                List[i+1] = List[i]
                List[i] = value
                i -= 1
            else: #Breaks when the list is done
                break
    
    
        
def query_grades_section():
    '''
Shows the records filtered by grades or section number.
No parameter or returns,
prints records that applies to the filter.
    '''
    global full_database
    print('Query for grade or section?')
    print('G for Grade.')
    print('S for Section.')
    decision = input('Enter your decision:')
    #Input validation
    while decision != 'G' and decision != 'S':
        print('Invalid input, try again.')
        decision = input('Please enter either G or S:')
    if decision == 'G':
        grade_thresh = input('Please enter a grade threshold:')
        grade_thresh = float(grade_thresh)
        #Threshold validation
        while grade_thresh < 0 or grade_thresh > 100:
            print('Invalid threshold for grades, please try again.')
            grade_thresh = float(input('Reenter a grade threshold:'))
        #Grabs the records that apply to the grade threshold
        for record in full_database:
            if record[3] >= grade_thresh:
                print(record)
    elif decision == 'S':
        sect_num = input('Enter a section number:')
        sect_num = int(sect_num)
        #Threshold validation
        while sect_num < 40 or sect_num > 43:
            print('Invalid section number.')
            sect_num = int(input('Please reenter a section number:'))
        #Grabs records with that section number
        for record in full_database:
            if record[2] == sect_num:
                print(record)

def chart():
    '''
Creates a pie chart from the grades from the full_database.
No parameters, returns a pie chart with labels and percentages.
    '''
    global full_database
    import matplotlib.pyplot as plt
    #Setting accumulators
    F_grade= 0
    D_grade= 0
    C_grade= 0
    B_grade= 0
    A_grade= 0
    #Goes through and sorts the grades into categories
    for record in range(len(full_database)):
        #Grabs only the grades
        grade = full_database[record][3]
        if grade >= 0 and grade < 60:
            F_grade += 1
        elif grade >= 60 and grade < 70:
            D_grade += 1
        elif grade >= 70 and grade < 80:
            C_grade += 1
        elif grade >= 80 and grade < 90:
            B_grade += 1
        elif grade >= 90 and grade <= 100:
            A_grade += 1
    Grade_Count = [F_grade, D_grade, C_grade, B_grade, A_grade]
    plt.title("Grades Spread Via Pie Chart")
    Grades = ['F', 'D', 'C', 'B', 'A']
    plt.pie(Grade_Count, labels=Grades, autopct='%1.0f%%')
    plt.show()            
    
        
            
def main():
    '''
Main function where every other function is called.
Presents menu, handles invalid and valid menu input,
and continues until user exits. No parameters or returns.
Functions that can be called:
    welcome()
    menu()
    bye()
    delete()
    chart()
    find_record()
    insert_record()
    print_database()
    read_and_merge()
    query_grades_section()
    
    '''
    #To make stop read and merge from being called again
    global Extra
    Extra = 0
    welcome()
    menu()
    choice = input("Enter your choice:")
    #While loop to make sure read and merge gets called first
    while Extra == 0:
        if choice == 'e':
            bye()
            quit()
        elif choice == 'r':
            read_and_merge()
        else:
            print('''
You must use the read and merge (r) function before
any other funtion, or exit the program.
''')
        #Returns user to menu
        print('.....Returning to menu')
        menu()
        choice = input("Enter your choice:")
    #While loop process valid and invalid choices
    while choice != 'e':
        if choice == 'd':
            delete()
        elif choice == 'f':
            find_record()
        elif choice == 'c':
            chart()
        elif choice == 'i':
            insert_record()
        elif choice == 'p':
            print_database()
        elif choice == 'r':
            print('''
Read and merge (r) has already been performed, and it
can only be ran once during this program.
    ''')
        elif choice == 'q':
            query_grades_section()
        #When invalid choice is used
        else:
            print("Invalid menu choice...")
        #Returns user to menu
        print('.....Returning to menu')
        menu()
        choice = input("Enter your choice:")
    #Quits the program when e is selected, calls bye()
    if choice == 'e':
        bye()
        quit()
main()       
