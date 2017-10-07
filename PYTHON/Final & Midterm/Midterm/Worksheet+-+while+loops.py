# Make sure you understand why each loop creates the output that it does.
# Convert the following while loops to for loops.
# For example, exercise 12b would be:
product = 1
n = 2
for k in range(0, 9, 4):
    product = product * n
print(product)


print("Exercise 1a")
x = 0
while x < 20:
    x = x + 1
    print(x)

print("Exercise 1b")
x = 0
while x < 20:
    print(x)
    x = x + 1
    
print("Exercise 2a")
x = 0
while x < 20:
    x = x + 1
print(x)

print("Exercise 2b")
x = 0
while x <= 20:
    x = x + 1
print(x)

print("Exercise 3a")
x = 10
while x > 0:
    x = x - 1
    print (x)

print("Exercise 3b")
x = 10
while x > 0:
    print (x)
    x = x - 1
    
print("Exercise 4")
x = 10
while x > 0:
    x = x - 1
print (x)

print("Exercise 5")
sum = 0
k = 0
while k <= 5:
    sum = sum + k
    print(sum)
    k = k + 1

print("Exercise 6a")
sum = 0
k = 0
while k <= 5:
    sum = sum + k
    k = k + 1
print (sum)

print ("Exercise 6b")
sum = 0
k = 0
while k <= 5:
    k = k + 1
    sum = sum + k
print(sum)

print("Exercise 6c")
sum = 0
k = 0
while k <= 10:
    k = k + 2
    sum = sum + k
print(sum)

print("Exercise 7")
sum = 0
k = 0
while k <= 5:
    sum = k 
    k = k + 1
    print(sum)

print("Exercise 8")
product = 0
k = 1
while k <= 5:
    product = product * k 
    k = k + 1
    print(product)

print("Exercise 9a")
product = 1
k = 1
while k <= 5:
    product = product * k 
    k = k + 1
    print(product)

print("Exercise 9b")
product = 1
k = 0
while k <= 5:
    k = k + 1
    product = product * k 
    print(product )   

print("Exercise 10")
product = 1
k = 1
while k <= 5:
    product = product * k 
    k = k + 1
print(product)

print("Exercise 11a")
sum = 1
k = 1
while k <= 5:
    sum = sum * k 
    k = k + 1
print(sum)

print("Exercise 11b")
product = 1
k = 1
while k <= 10:
    product = product * k 
    k = k + 2
print(product)

print("Exercise 11c")
product = 1
k = 0
while k <= 8:
    k = k + 2
    product = product * k 
    print (product)

print("Exercise 12a")
product = 1
n = 2
k = 0
while k <= 8:
    k = k + 2
    product = product * n 
    print (product)

print("Exercise 12b")
product = 1
n = 2
k = 0
while k <= 11:
    k = k + 2
    product = product * n
    k = k + 2
print(product)

product = 1
n = 2
for k in range(0, 9, 4):
    product = product * n
print(product)
