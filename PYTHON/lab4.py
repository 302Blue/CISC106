#Andrew Baldwin
from cisc106_34 import assertEqual
import matplotlib

#Problem 1
print()
print('Problem 1')
def compute_md5_hash(my_string):
    '''
Takes a string and returns that string encoded in md5 hash.
Parameters:
    my_string (string) - string to be converted
Returns:
    hex_string (bytes) - converted version of string
    '''
    import hashlib
    #transforms string into bytes
    hash_object = hashlib.md5(my_string.encode())
    #encodes the string
    hex_string = hash_object.hexdigest()
    return(hex_string)

assertEqual(compute_md5_hash('hi'),'49f68a5c8493ec2c0bf489821c21fc3b')
assertEqual(compute_md5_hash('drew'),'b2dd08a69dcdac5a20a7b90b5c4b759f')
assertEqual(compute_md5_hash('bye'),'bfa99df33b137bc8fb5f5407d7e58da8')



#Problem 2
print()
print('Problem 2')
def convert_to_base64(my_string):
    '''
Takes a string and converts it to b64 encoding.
Parameters:
    my_string (string) - string to be converted
Returns:
    encoded_string (bytes) - transformed version of string
    '''
    import base64
    #encodes and converts the string in the same line
    encoded_string = base64.b64encode(bytes(my_string,"utf-8"))
    return(encoded_string)

assertEqual(convert_to_base64('hi'),b'aGk=')
assertEqual(convert_to_base64('drew'),b'ZHJldw==')
assertEqual(convert_to_base64('bye'),b'Ynll')

#Problem 3
print()
print('Problem 3')
def convert_from_base64(byte_string):
    '''
Decodes a byte string from base64 to a regular string.
Parameters:
    byte_string (bytes) - bytes to be decoded
Returns:
    decoded_string (string) - original string returned
    '''
    import base64
    #decodes back to normal string
    decoded_string = base64.b64decode(byte_string)
    #takes the b' moniker off the string
    decoded_string = decoded_string.decode()
    return(decoded_string)
assertEqual(convert_from_base64(b'aGk='),'hi')
assertEqual(convert_from_base64(b'ZHJldw=='),'drew')
assertEqual(convert_from_base64(b'Ynll'),'bye')



#Problem 4
print()
print('Problem 4')
def quadratic_roots(a,b,c):
    '''
Finds the quadriatic roots of a function
Parameters:
    a (float or int) - first coefficient
    b (float or int) - second coefficient
    c (float or int) - third coefficient
Returns:
    root_list (list) - list of the possible roots (empty if invalid inputs)
    '''
    import math
    root_list = []
    #parameter testing
    if (type(a) != int and type(a) != float) or (type(b) != int \
    and type(b) != float) or (type(c) != int and type(c) != float):
        print('All parameters must either be integers or floats')
        return None
    else:
        #convert all parameters to float
        a = float(a)
        b = float(b)
        c = float(c)
        #discriminant determines whether there will be 0,1, or 2 roots
        discriminant = (b**2) - (4*a*c)
        #for linear root
        if a == 0 and b != 0 and c != 0:
            root = -c/b
            root_list.append(root)
            return root_list
        #no real roots
        elif a == 0 and b == 0 and c != 0:
            return root_list
        #equation = 0, no root b/c no equation
        elif a == 0 and b == 0 and c == 0:
            return root_list
        else:
            #no real roots
            if discriminant < 0:
                print('This equation doesn\'t have any real roots')
                return root_list
            #one root
            elif discriminant == 0:
                root = ((-b)+math.sqrt(discriminant))/(2*a)
                root_list.append(root)
                return root_list
            #two roots
            else:
                root1 = ((-b)-math.sqrt(discriminant))/(2*a)
                root2 = ((-b)+math.sqrt(discriminant))/(2*a)
                root_list.append(root1)
                root_list.append(root2)
                return root_list    
                print('The roots for this equation are', root1, 'and', root2)
assertEqual(quadratic_roots(1,4,4),[-2.0])
assertEqual(quadratic_roots(0,0.0,0),[])
assertEqual(quadratic_roots(1,2,6),[])
assertEqual(quadratic_roots(1,2,'hi'),None)
assertEqual(quadratic_roots([1],2,3),None)
assertEqual(quadratic_roots(True,False,True),None)

#Problem 5
print()
print('Problem 5')
def convert_10_to_16(number):
    '''
Converts a base 10 number to a base 16 hexadecimal number
Parameter:
    number (integer) - Positive integer to be converted
Return: Varies
    a string that is the hexadecimal version of the parameter(w/o 0x)
    '''
    if (type(number) == int) and (number >= 0):
        remainder = number % 16
        new_number = number // 16
        #stops infinite loops, when last digit constantly repeats
        if (remainder == 0 and new_number != 0):
            return('')
        #makes it so an unnecessary 0 isn't added
        elif (remainder != 0 and new_number == 0):
            return(hex(remainder)[2:])
        #for when just a zero is inputed
        elif remainder == 0 and new_number == 0:
            return(hex(0)[2:])
        else:
        #adds converted hex digit to the next until none left can be converted
            return(convert_10_to_16(new_number)+hex(remainder).lstrip('0x'))
    else:
        print('The parameter must be a positive base 10 integer')
        return None
print(convert_10_to_16(5))
assertEqual(convert_10_to_16(483),'1e3')
assertEqual(convert_10_to_16(0),'0')
assertEqual(convert_10_to_16(1),'1')
assertEqual(convert_10_to_16(-1),None)
assertEqual(convert_10_to_16(5.5),None)
assertEqual(convert_10_to_16('hi'),None)

#Problem 6
print()
print('Problem 6')
def plot_chem_eng_101_grades(grades):
    '''
Plots a class's grades in pie chart and histogram form
Parameters:
    grades (list) - A list of grades in the class from 0 to 100
Returns:
    True (bool) - when valid input is recieved and plots can be made
    False (bool) - when invalid input is recieved
    '''
    import matplotlib.pyplot as plt
    #setting up accumulators
    F_grade= 0
    D_grade= 0
    C_grade= 0
    B_grade= 0
    A_grade= 0
    Grade_List = []
    if type(grades) == list:
        for value in grades:
            if type(value)==int or type(value)==float:
                #Setting up percents and pieces for Pie Chart
                if value >= 0 and value < 60:
                    F_grade += 1
                    Grade_List.append(value)
                elif value >= 60 and value < 70:
                    D_grade += 1
                    Grade_List.append(value)
                elif value >= 70 and value < 80:
                    C_grade += 1
                    Grade_List.append(value)
                elif value >= 80 and value < 90:
                    B_grade += 1
                    Grade_List.append(value)
                elif value >= 90 and value <= 100:
                    A_grade += 1
                    Grade_List.append(value)
                else:
                    #When grades are outside the range
                    return False
                    print('Grades must be between 0 to 100')
            else:
                #When list contains an invalid input
                return False
                print('List must contain only integer and float values')
    else:
        #When parameter isn't a list
        return False
        print('Parameter must be a list')
    #Pie Chart
        #Variable for Pie Chart data
    Grade_Count = [F_grade, D_grade, C_grade, B_grade, A_grade]
    plt.title('Chemical Engineering 101 Grades')
        #Variable to show labels
    Grades = ['F', 'D', 'C', 'B', 'A']
    plt.pie(Grade_Count, labels=Grades, autopct='%1.2f%%')
    plt.show()
    #Histogram
        #Variable for Histogram bins
    bins = [0, 60, 70, 80, 90, 100]
    plt.title('Chemical Engineering 101 Grades')
    plt.xlabel('Grades')
    plt.ylabel('Number of Grades')
    plt.hist(Grade_List, bins)
    plt.show()
    return True
    
assertEqual(plot_chem_eng_101_grades([40, 50, 60, 65, 75, 77, 85,\
86.5, 87, 90, 98, 99, 100]), True)
assertEqual(plot_chem_eng_101_grades('grades'), False)
assertEqual(plot_chem_eng_101_grades([True, True]), False)
assertEqual(plot_chem_eng_101_grades([-1, -55, -70]),False)


#Problem 7
print()
print('Problem 7')
def weighted_filter(raw_data_filename, filtered_data_filename):
    '''
Finds a weighted average 3 lines at a time from a file and puts the
wighted value into a new file. Also creates a plot of each file's data.
Parameters:
    raw_data_filename (string) - filename to read data from
    filtered_data_filename (string) - filename to write data to
Returns:
    None
    '''
    import matplotlib.pyplot as plt
    import numpy as np
    #Opening files
    Raw = open(raw_data_filename, 'r')
    Filtered = open(filtered_data_filename, 'w')
    #Sets variables to zero
    raw_data_list = []
    filtered_data_list = []
    line1 = 0
    line2 = 0
    line3 = 0
    line_count = 0
    #Read each line for data
    for line in Raw:
        line_count += 1
        line1 = line2
        line2 = line3
        #Strips newline character from incoming lines
        line3 = float(line.rstrip('\n'))
        #Add to list for Data plot
        raw_data_list.append(line3)
        #computing weighted average after getting 3 numbers
        if line_count >= 3:
            Filter = (line1 + 2*line2 + line3)/4
            #Stop the decimels from going to far
            Filter = format(Filter,'.2f')
            #Write weighed average to new file
            Filtered.write(Filter + '\n')
            #Add to list for Data plot
            filtered_data_list.append(Filter)
    #Data plot
    plt.plot(raw_data_list)
    plt.plot(filtered_data_list)
    plt.legend(["Raw", "Filtered"], loc='best')
    plt.title('Raw and Smooth Data Plot')
    plt.show()
    #Closing files
    Raw.close()
    Filtered.close()
weighted_filter(r'C:\Users\Drew\Documents\CISC106\Work\hi.txt', r'C:\Users\Drew\Documents\CISC106\Work\hi2.txt')

#Problem 8
print()
print('Problem 8')
def input_roster():
    '''
Reads a roster of names sorted by last name first and resorts
them into a new roster file by first name first.
Parameters:
    None
Returns:
    None
    '''
    file_name = str(input('What is the name of your roster file?'))
    #Opens files
    Roster = open(file_name, 'r')
    New_file = open('roster_first_last.txt','w')
    #Reads first line
    line = Roster.readline()
    #While statment to stop when it gets to the end of the file
    while line != '':
        #Strips newline character
        line = line.rstrip('\n')
        #Makes the line into a list
        split = line.split(",")
        #Takes the first name out of the list
        first_name = split[1:2]
        #Takes the last name out of the list
        last_name = split[0:1]
        #Resorts the list by first name first
        Full_name = first_name + last_name
        #Makes the list back into a string & adds newline
        Name_string = (' '.join(map(str,Full_name))) + '\n'
        #Writes the sorted name to a new file
        New_file.write(Name_string)
        #Restarts the process with a new line
        line = Roster.readline()
    #Closes the files
    Roster.close()
    New_file.close()

            
    
        
        
