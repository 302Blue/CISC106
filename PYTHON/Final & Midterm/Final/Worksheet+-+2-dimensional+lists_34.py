# You are given the following 2D list sorted in asccending order
# according to the first element (primary key) in each record.

[[10, 'Tom', 14.7, True],
 [14, 'Sue', 37.5, False],
 [21, 'Joe', 55.3, False],
 ...
 ...
 ...
 [33, 'Ann', 46.2, False],
 [48, 'Art', 37.5, True]]
 
# Solve the following exercises. You may want to copy the above sample
# database into a Python file, assign it to a variable, add a few more
# records to it, and test your solutions.

# Exercise 1: Print the first and second field for all records, one
# record per line.
 10 'Tom'
 14 'Sue'
 21 'Joe'
 ...
 ...
 ...
 33 'Ann'
 48 'Art'
 
# Exercise 2: Print all records, one per line, but only include the
# first two fields in each record.
 [10, 'Tom']
 [14, 'Sue']
 [21, 'Joe']
 ...
 ...
 ...
 [33, 'Ann']
 [48, 'Art']
 
# Exercise 3: Print all False records 
 [14, 'Sue', 37.5, False]
 [21, 'Joe', 55.3, False]
 ...
 ...
 ...
 [33, 'Ann', 46.2, False]
 
# Exercise 4: Print all False records, excluding the 3rd field in each record.
 [14, 'Sue', False]
 [21, 'Joe', False]
 ...
 ...
 ...
 [33, 'Ann', False]
 
# Exercise 5: Print the full list in descending order
 [48, 'Art', 37.5, True]
 [33, 'Ann', 46.2, False]
 ...
 ...
 ...
 [21, 'Joe', 55.3, False] 
 [14, 'Sue', 37.5, False]
 [10, 'Tom', 14.7, True]


 
 
"""
Assume a database of records named 'Students' exists in memory
where each record is represented as a list.  A record contains 
a student's last name, first name, student ID number, age, amount 
of money owed to the university, father's first name, 
mother's first name, and class year.  Assume the database is sorted
according to last name (primary key).  If multiple students
have the same last name, assume their records are sorted by student's
first name (secondary key).

Some example records would be:
  ['Brooks', 'Kim', 718337185, 18, 0.0, 'Christopher', 'Christine', 'freshman']
  ['Daniels', 'Chester', 797701002, 18, 8220.01, 'Charlie', 'Beverly', 'freshman']
  ['Daniels', 'Chris', 810199144, 20, 0.0, 'Jack', 'Clair', 'senior']
  ['Jones', 'Joe', 700157834, 19, 17395.57, 'Daniel', 'Susan', 'junior']
  ['Lowenstern', 'Ike', 877377100, 21, 813.3, 'Jacob', 'Laura', 'senior']
  ['Updegrave', 'Douglas', 711922910, 19, 0.0, 'Philip', 'Leticia', 'sophomore']
"""

# Write Python code that will print the following:
# Exercise 1 - full records of the entire database, one per line

# Exercise 2 - full records of students that are seniors

# Exercise 3 - full records of students over the age of 19 and whose
# last name starts with 'J'

# Exercise 4 - student id numbers for students that have an outstanding
# balance to pay the university

# Exercise 5 - first and last names of all students who are teenagers

# Exercise 6 - for all students that are freshman and have a first name
# with exactly 3 letters, print the name of the parent that comes first
# alphabetically
