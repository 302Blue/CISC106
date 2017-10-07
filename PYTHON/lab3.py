##Andrew Baldwin and Nicholas Trieu
from cisc106_34 import assertEqual

#Problem 1 -- assert and comment
print()
print('Problem 1')
def count_mult3_ints(Multiple3_List):
    Nums_in_list = 0
    for value in Multiple3_List:
        if ((value % 3) == 0) and (type(value) == int):
            Nums_in_list = int(Nums_in_list) + 1
    return(Nums_in_list)

##assertEqual()
##assertEqual()
##assertEqual()
##assertEqual()

#Problem 2 -- assert and comment
print()
print('Problem 2')
def sum_even_ints(User_List):
    Sum = 0
    for value in User_List:
        if ((value % 2) == 0) and (type(value) == int):
            Sum = Sum + value
    if Sum == 0:
        return None
    return(Sum)

##assertEqual()
##assertEqual()
##assertEqual()
##assertEqual()

#Problem 3 -- Doesn't work
print()
print('Problem 3')
def insert_list(Int_List,Number):
    if type(Number) != int:
        print("Variable error, second parameter must be an integer to be inserted")
        return None
    TestVariable = 0
    for TestVariable in Int_List:
        if type(TestVariable) != int or (Int_List[0] > Int_List[1]) or (Int_List[1] > Int_List[2])\
           or (Int_List[2] > Int_List[3]) or (Int_List[3] > Int_List[4]) or (Int_List[4] > Int_List[5])\
           or (Int_List[5] > Int_List[6]):
            print("ListError, list must contain only variables in increasing order")
        else:
            print(None)
            
            
            

##assertEqual()
##assertEqual()
##assertEqual()
##assertEqual()

#Problem 4 -- assert and comment
print()
print('Problem 4')
def distance(x1,y1,x2,y2):
    from math import sqrt
    if (type(x1) != int) or (type(y1) != int) or (type(x2) != int) or (type(y2) != int) or \
    (type(x1) != float) or (type(y1) != float) or (type(x2) != float) or (type(y2) != float):
        print("Variable error, all variables must be numbers")
        distance = None
    else:
        distance = sqrt((x2 - x1)**2 +(y2 - y1)**2)
    return(distance)

##assertEqual()
##assertEqual()
##assertEqual()
##assertEqual()


#Problem 5 -- assert and comment
print()
print('Problem 5')
def assert_within_tolerance(numbr1,numbr2,tolerance):
    if type(numbr1) != float or type(numbr2) != float or type(tolerance) != float or tolerance < 0:
        print('Invalid inputs, all values must be floats and the tolerance variable must be positive')
        return None
    else:
        if numbr1 + tolerance >= numbr2 or numbr2 - tolerance <= numbr1:
            return True
        else:
            return False

##assertEqual()
##assertEqual()
##assertEqual()
##assertEqual()

        
#Problem 6 -- assert and comment
print()
print('Problem 6')
def word_seperator(string):
    i = 0
    result = ""
    for letter in string:
        if letter.isupper() and i>0:
            result = result + " "
            result = result + letter.lower()
        else:
            result = result + letter
        i = i + 1
    return(result)

##assertEqual()
##assertEqual()
##assertEqual()
##assertEqual()


#Problem 7 -- Doesn't work
print()
print('Problem 7')
def word_parser(mystring):
    mylist = []
    return None

##assertEqual()
##assertEqual()
##assertEqual()
##assertEqual()


#Problem 8 -- assert and comment
print()
print('Problem 8')
def digit_sum(dig_str):
    dig_sum = 0
    if dig_str == "" or dig_str == " ":
        print('String list cannot be empty, add integers.')
        return None
    dig_str = list(dig_str)
    for letter in dig_str:
        if letter not in ['0', '1','2','3','4','5','6','7','8','9']:
            print('String list must contain integers only.')
            return None
        else:
            dig_sum = dig_sum + int(letter) 
    return dig_sum

##assertEqual()
##assertEqual()
##assertEqual()
##assertEqual()


#Problem 9 -- assert and comment
print()
print('Problem 9')
def valid_password(password):
    invalid = 0
    valid1= 0
    if len(password) >= 8 and len(password) <= 12:
        valid1 = valid1 + 1
    else:
        invalid = invalid + 1
    valid2 = 0
    valid3 = 0
    valid4 = 0
    valid5 = 0
    for character in password:
        if character.isupper():
            valid2 = valid2 + 1
        elif character.islower():
            valid3 = valid3 + 1
        elif character.isdigit():
            valid4 = valid4 + 1
        elif character in ['!','#','$','%','&','*','+','=']:
            valid5 = valid5 + 1
        else:
            invalid = invalid + 1
    if invalid == 0 and valid1 > 0 and valid2 > 0 and valid3 > 0 \
    and valid4 > 0 and valid5 > 1:
        return True
    else:
        if valid1 == 0:
            print('Invalid password, password must be between 8 to 12 characters.')
        if valid2 == 0:
            print('Password must contain at least one uppercase character.')
        if valid3 == 0:
            print('Password must contain at least one lowercase character.')
        if valid4 == 0:
            print('Password must contain at least one digit.')
        if valid5 == 0:
            print('Password must contain at least two of the special characters\
"!,#,$,%,&,*,+,="')
        return False
        
    
valid_password("Hi55##19701")
    

            
    
        

        
            
