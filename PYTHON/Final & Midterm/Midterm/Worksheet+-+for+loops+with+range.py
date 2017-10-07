# Make sure you understand why each loop creates the output that it does.
# Convert all the following for loops to while loops.
# For example, the Exercise 20 would be:
u = 3           # loop variable = start
while u < 10:   # while loop variable < stop  (assuming step is +)
    sum = u * 5
    u = u + 3   # loop variable = loop variable + step
print (sum)


print ("Exercise 1")
for i in range (10):
    print (i)

print ("Exercise 2")
for i in range (6):
    print (i)

print ("Exercise 3")
for i in range (2,7):
    print (i)

print ("Exercise 4")
for i in range (1,10):
    print (i)

print ("Exercise 5")
for d in range (9, 14):
    print (d)
    
print ("Exercise 6")
for i in range (10,1,-1):
    print (i)

print ("Exercise 7")
for y in range (3,10,2):
    print (y)

print ("Exercise 8")
for i in range (1100, 1110, 5):
    print (i)

print ("Exercise 9")
for r in range (980, 970, -3):
    print (r)

print ("Exercise 10")
t = 0
for i in range (8):
    t = t + 1
    print (t)

print ("Exercise 11")
t = 0
for i in range (8):
    print (t)
    t = t + 1
    
print ("Exercise 12")
t = 0
for i in range (8):
    t = t + 2
print (t)

print ("Exercise 13")
sum = 0
for i in range (5):
    sum = sum + 1
print (sum)

print ("Exercise 14")
sum = 0
for i in range (5):
    sum = sum + i
    print (sum)

print ("Exercise 15")
sum = 0
for i in range (10):
    print (sum)
    sum = sum + i

print ("Exercise 16")
sum = 0
for i in range (5):
    print (sum)
    sum = sum * i

print ("Exercise 17")
j = 0
for i in range (6):
    j = j - 4
print (j)

print ("Exercise 18")
for u in range (3,9,3):
    sum = u * 5
    print (sum)

print ("Exercise 19")
for u in range (3,10,3):
    sum = u * 5
    print (u)

print ("Exercise 20")
for u in range (3,10,3):
    sum = u * 5
print (sum)
