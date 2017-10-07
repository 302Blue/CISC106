 ##Andrew Baldwin (worked alone)
from random import randint
from cisc106_34 import assertEqual

##Sets the initial values for the extra credit "Counting" variables
global First_Try
First_Try = 0
global Scnd_Try
Scnd_Try = 0
global Thrd_Try
Thrd_Try = 0
global Incorrect
Incorrect = 0

def welcome():
    '''
Prints a simple welcome message.
No parameters or returns.
    '''
    print('''
    ----------------------------------------------------------------------------
    Welcome to CISC106 Math Teacher. This program will help you improve your
    math skills by supplying as many Addition, Subtraction, Multiplication,
    Division, and Exponentiation practice problems as you wish.
    ----------------------------------------------------------------------------
    ''')
    

def menu():
    '''
Explains to the user how to start using the program by providing a list of valid
menu options for the user, and explaining what each one does.
No parameters or returns.
    '''
    print('''
    ________________________________Main Menu___________________________________
    To begin using this program please type a letter for which math skill you
    would like to practice;
                           a for Addition
                           s for Subtraction
                           m for Multiplication
                           d for Division
                           e for Exponentiation
                           r for Random
                           q to Quit the program
    ____________________________________________________________________________
    ''')
          
    
def bye():
    '''
Displays how many problems the user got right on what try, and how many they got
wrong. Also displays the program's goodbye message.
No parameters or returns.
    '''
    print("You answered", First_Try, 'questions right on the first try,')
    print(Scnd_Try,'right on the second try, and', Thrd_Try,'right on the third try.')
    print("You answered", Incorrect, "problems incorrectly.")
    print("Thank you for using CISC106 Math Teacher, goodbye.")

def addition():
    '''
Randomly generates an addition question with two numbers in between 0 and 15.
Gives the user 3 tries before displaying the correct questions
No parameters or returns.
    '''
    print()
    Correct = False
    while Correct == False:
        augend = randint(0,15)
        addend = randint(0,15)
        addition_question = "How much is " + str(augend) + "+" + str(addend) + "?"
        answer = int(input(addition_question))
        real_answer = int(augend) + int(addend)
        if int(answer) != real_answer:
            Correct = False
            answer = input("Sorry that is incorrect, please try again:")
            if int(answer) != real_answer:
                Correct = False
                answer = input("Sorry that is incorrect, please try again:")
                if int(answer) != real_answer:
                    Correct = True
                    print("Oops you didn't get this, the real answer is: ", real_answer)
                    global Incorrect
                    Incorrect = Incorrect + 1
                else:
                    Correct = True
                    global Thrd_Try
                    Thrd_Try = Thrd_Try + 1
                    print('Correct')
            else:
                Correct = True
                global Scnd_Try
                Scnd_Try = Scnd_Try + 1
                print('Correct')
        else:
            Correct = True
            global First_Try
            First_Try = First_Try + 1
            print('Correct')
    print()
        
    
def subtraction():
    '''
Randomly generates a subtraction question with two values in between 0 and 15,
while also ensuring the answer cannot be negative. Gives the user 3 tries
before displaying the correct answer.
No parameters or returns.
    '''
    print()
    Correct = False
    while Correct == False:
        minuend = randint(0,15)
        subtrahend = randint(0,15)
        while subtrahend > minuend:
            subtrahend = randint(0,15)
        subtraction_question = "How much is " + str(minuend) + "-" + str(subtrahend) + "?"
        answer = int(input(subtraction_question))
        real_answer = int(minuend) - int(subtrahend)
        if int(answer) != real_answer:
            Correct = False
            answer = input("Sorry that is incorrect, please try again:")
            if int(answer) != real_answer:
                Correct = False
                answer = input("Sorry that is incorrect, please try again:")
                if int(answer) != real_answer:
                    Correct = True
                    print("Oops you didn't get this, the real answer is: ", real_answer)
                    global Incorrect
                    Incorrect = Incorrect + 1
                else:
                    Correct = True
                    global Thrd_Try
                    Thrd_Try = Thrd_Try + 1
                    print('Correct')
            else:
                Correct = True
                global Scnd_Try
                Scnd_Try = Scnd_Try + 1
                print('Correct')
        else:
            Correct = True
            global First_Try
            First_Try = First_Try + 1
            print('Correct')
    print()

def multiplication():
    print()
    '''
Randomly generates a multiplication question with two values in between 0 and 12.
Gives the user 3 tries before displaying the correct answer.
No parameters or returns.
    '''
    Correct = False
    while Correct == False:
        multiplicand = randint(0,12)
        multiplier = randint(0,12)
        multiplication_question = "How much is " + str(multiplicand) + "*" + str(multiplier) + "?"
        answer = int(input(multiplication_question))
        real_answer = int(multiplicand) * int(multiplier)
        if int(answer) != real_answer:
            Correct = False
            answer = input("Sorry that is incorrect, please try again:")
            if int(answer) != real_answer:
                Correct = False
                answer = input("Sorry that is incorrect, please try again:")
                if int(answer) != real_answer:
                    Correct = True
                    print("Oops you didn't get this, the real answer is: ", real_answer)
                    global Incorrect
                    Incorrect = Incorrect + 1
                else:
                    Correct = True
                    global Thrd_Try
                    Thrd_Try = Thrd_Try + 1
                    print('Correct')
            else:
                Correct = True
                global Scnd_Try
                Scnd_Try = Scnd_Try + 1
                print('Correct')
        else:
            Correct = True
            global First_Try
            First_Try = First_Try + 1
            print('Correct')
    print()
    
def division():
    '''
Randomly generates a division question with two values in between 1 and 12,
while also ensuring the answer cannot have a remainder or a value outside the
range of 0,12. Gives the user 3 tries before displaying the correct answer.
No parameters or returns.
    '''
    print()
    Correct = False
    while Correct == False:
        dividend = randint(1,12)
        divisor = randint(1,12)
        while ((dividend % divisor) != 0) or  ((dividend / divisor) > 12):
            divisor = randint(1,12)
        division_question = "How much is " + str(dividend) + "/" + str(divisor) + "?"
        answer = int(input(division_question))
        real_answer = int(dividend) / int(divisor)
        if int(answer) != real_answer:
            Correct = False
            answer = input("Sorry that is incorrect, please try again:")
            if int(answer) != real_answer:
                Correct = False
                answer = input("Sorry that is incorrect, please try again:")
                if int(answer) != real_answer:
                    Correct = True
                    print("Oops you didn't get this, the real answer is: ", real_answer)
                    global Incorrect
                    Incorrect = Incorrect + 1
                else:
                    Correct = True
                    global Thrd_Try
                    Thrd_Try = Thrd_Try + 1
                    print('Correct')
            else:
                Correct = True
                global Scnd_Try
                Scnd_Try = Scnd_Try + 1
                print('Correct')
        else:
            Correct = True
            global First_Try
            First_Try = First_Try + 1
            print('Correct')
    print()
    
def exponentiation():
    '''
Randomly generates an exponentiation question with two values in between
0 and 10, while also ensuring the answer cannot be more than 4100.
Gives the user 3 tries before displaying the correct answer.
No parameters or returns.
    '''
    print()
    Correct = False
    while Correct == False:
        base = randint(0,10)
        exponent = randint(0,10)
        while (base ** exponent) > 4100:
            base = randint(0,10)
        exponentiation_question = "How much is " + str(base) + "^" + str(exponent) + "?"
        answer = int(input(exponentiation_question))
        real_answer = int(base) ** int(exponent)
        if int(answer) != real_answer:
            Correct = False
            answer = input("Sorry that is incorrect, please try again:")
            if int(answer) != real_answer:
                Correct = False
                answer = input("Sorry that is incorrect, please try again:")
                if int(answer) != real_answer:
                    Correct = True
                    print("Oops you didn't get this, the real answer is: ", real_answer)
                    global Incorrect
                    Incorrect = Incorrect + 1
                else:
                    Correct = True
                    global Thrd_Try
                    Thrd_Try = Thrd_Try + 1
                    print('Correct')
            else:
                Correct = True
                global Scnd_Try
                Scnd_Try = Scnd_Try + 1
                print('Correct')
        else:
            Correct = True
            global First_Try
            First_Try = First_Try + 1
            print('Correct')
    print()
    
def random():
    '''
Randomly chooses from one of the above functions by picking a random
value and assigning that value to one of the functions.
Returns the choice variable, which is reused by main to open one of the
other if statements.
Returns:
    Choice:(string)-letter that corresponds to one of the other functions.
    '''
    function = randint(1,5)
    if int(function) == 1:
        choice = 'a'
    elif int(function) == 2:
        choice = 's'
    elif int(function) == 3:
        choice = 'm'
    elif int(function) == 4:
        choice = 'd'
    else:
        choice = 'e'
    return(choice)

def main():
    '''
This function displays the user menu and processes user input from that menu. Also
where goodbye function is called when the user quits.
No parameters or returns.
    '''
    menu() #Calls the menu list.
    choice = input("Enter your choice for what you would like to practice:")
    #While loop to process valid menu choices and invalid choices.
    while choice != 'q':
        if choice == 'a':
            ques_num = 4
            print("You have choosen Addition")
            while int(ques_num) > 0:
                ques_num = int(ques_num) - 1
                addition()
            print('...Returning to menu')
            menu()
            choice = input("Enter your choice for what you would like to practice:")            
        elif choice == 's':
            ques_num = 4
            print("You have choosen Subtraction")
            while int(ques_num) > 0:
                ques_num = int(ques_num) - 1
                subtraction()
            print('...Returning to menu')
            menu()
            choice = input("Enter your choice for what you would like to practice:")
        elif choice == 'm':
            ques_num = 4
            print("You have choosen Multiplication")
            while int(ques_num) > 0:
                ques_num = int(ques_num) - 1
                multiplication()
            print('...Returning to menu')
            menu()
            choice = input("Enter your choice for what you would like to practice:")
        elif choice == 'd':
            ques_num = 4
            print("You have choosen Division")
            while int(ques_num) > 0:
                ques_num = int(ques_num) - 1
                division()
            print('...Returning to menu')
            menu()
            choice = input("Enter your choice for what you would like to practice:")
        elif choice == 'e':
            ques_num = 4
            print("You have choosen Exponentiation")
            while int(ques_num) > 0:
                ques_num = int(ques_num) - 1
                exponentiation()
            print('...Returning to menu')
            menu()
            choice = input("Enter your choice for what you would like to practice:")
        elif choice == 'r':
            choice = random()
        #For when a choice is made that does not match one of the menu choices.    
        else: 
            menu()
            choice = input("Invalid menu choice, please try again:")
    #For when the user wants to use the "quit program" menu option.        
    if choice == 'q':
        bye() #Calls goodbye function.
        

welcome() #Calling the welcome message.        
main() #Calling main function


