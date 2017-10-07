Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 

---------------------------------------------------------------------------

Welcome to this the CISC106 Database System. This program allows the user to

interact simply with files in a database. Here, the user can create, modify,

and maintain a simple database.

---------------------------------------------------------------------------
    

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:f

You must use the read and merge (r) function before
any other funtion, or exit the program.

.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:r
What is the name of the first file?sample-r1.txt
What is the name of the second file?sample-r2.txt
The files have been read and merged together.
.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:r

Read and merge (r) has already been performed, and it
can only be ran once during this program.
    
.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:p

['Bud', 'Abbott', 41, 92.3]
['Don', 'Adams', 41, 90.4]
['Mary', 'Boyd', 42, 91.4]
['Jill', 'Carney', 43, 76.3]
['Rodney', 'Clifton', 40, 82.1]
['Diane', 'Keaton', 40, 61.1]
['Randy', 'Newman', 40, 41.2]

.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:f
What is the last name of the record you'd like to find?Invalid
Record does not exist.
.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:f
What is the last name of the record you'd like to find?Abbott
['Bud', 'Abbott', 41, 92.3]
.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:d
What is the last name of the record you'd like to delete?Invalid
Record does not exist.
.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:d
What is the last name of the record you'd like to delete?Abbott
Record has been deleted.
.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:p

['Don', 'Adams', 41, 90.4]
['Mary', 'Boyd', 42, 91.4]
['Jill', 'Carney', 43, 76.3]
['Rodney', 'Clifton', 40, 82.1]
['Diane', 'Keaton', 40, 61.1]
['Randy', 'Newman', 40, 41.2]

.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:i
What is the first name?Andrew
What is the last name?Baldwin
What is the section number?41
What is their grade?70
The record ['Andrew', 'Baldwin', 41, 70.0] has been successfully inserted.
.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:i
What is the first name?Andrew
What is the last name?Baldwin
Last name already in database.
Please reenter a last name:Louis
What is the section number?39
Invalid section number, try again.
Reenter a section number:40
What is their grade?-2
Invalid grade input.
Please reenter their grade:2
The record ['Andrew', 'Louis', 40, 2.0] has been successfully inserted.
.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:p

['Don', 'Adams', 41, 90.4]
['Andrew', 'Baldwin', 41, 70.0]
['Mary', 'Boyd', 42, 91.4]
['Jill', 'Carney', 43, 76.3]
['Rodney', 'Clifton', 40, 82.1]
['Diane', 'Keaton', 40, 61.1]
['Andrew', 'Louis', 40, 2.0]
['Randy', 'Newman', 40, 41.2]

.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:q
Query for grade or section?
G for Grade.
S for Section.
Enter you decision:r
Invalid input, try again.
Please enter either G or S:G
Please enter a grade threshold:50
['Don', 'Adams', 41, 90.4]
['Andrew', 'Baldwin', 41, 70.0]
['Mary', 'Boyd', 42, 91.4]
['Jill', 'Carney', 43, 76.3]
['Rodney', 'Clifton', 40, 82.1]
['Diane', 'Keaton', 40, 61.1]
.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:q
Query for grade or section?
G for Grade.
S for Section.
Enter you decision:p
Invalid input, try again.
Please enter either G or S:S
Enter a section number:41
['Don', 'Adams', 41, 90.4]
['Andrew', 'Baldwin', 41, 70.0]
.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:q
Query for grade or section?
G for Grade.
S for Section.
Enter you decision:G
Please enter a grade threshold:-2
Invalid threshold for grades, please try again.
Reenter a grade threshold:10
['Don', 'Adams', 41, 90.4]
['Andrew', 'Baldwin', 41, 70.0]
['Mary', 'Boyd', 42, 91.4]
['Jill', 'Carney', 43, 76.3]
['Rodney', 'Clifton', 40, 82.1]
['Diane', 'Keaton', 40, 61.1]
['Randy', 'Newman', 40, 41.2]
.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:q
Query for grade or section?
G for Grade.
S for Section.
Enter you decision:S
Enter a section number:39
Invalid section number.
Please reenter a section number:41
['Don', 'Adams', 41, 90.4]
['Andrew', 'Baldwin', 41, 70.0]
.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:g
Invalid menu choice...
.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:c
.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:r

Read and merge (r) has already been performed, and it
can only be ran once during this program.
    
.....Returning to menu

--------------------------------Main Menu------------------------------

Database functions:  

    d - delete record  

    f - find record  

    i - insert record  

    p - print database  

    r - read and merge  

    q - query grades and sections  

    c - chart grades in pie chart  

    e - exit program  

-----------------------------------------------------------------------
    
Enter your choice:e
Exiting program, goodbye
>>> 
