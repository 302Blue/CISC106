

if "Mark" <= "Mary":
    print('True')

if (not((5<3) or (8>5))) == False:
    print("False")

def summult(x,y):
    if (x>y):
        result = x*y
    else:
        result = x+y
    return(result)
x = summult(5,10)
print(x)

a=9
b=a
b=b-3
a=b+3
print(a,b)

m=11
n=77
n=m
m=n
print(n,m)

Sum=0
for b in [2,4,6,8]:
    Sum = Sum + b + 1
    print(Sum)

print(sum(range(-21,999,3)))

num = 85479
x = num // 1000
y = x % 10
print(y)

def h(x):
    return(x+5)
print(h(h(h(3))))

def bigger(x,y):
    if(x>y):
        print(x)
    else:
        print(y)
    return
x = bigger(11,12)
print(x)

d = True and True or False
t = True or False and True
q = False and False or True
if d == True:
    print('True')
if t == True:
    print('True')
if q == True:
    print('True')

#number = randint(1,50)
#print(number)

##The while loop is a pretest type of loop
##Posttest loops always test at least once
##Infinite loop loops until interrupted externeally

x = [3,6,9,12,15,18]
for i in [1,5,3]:
    print(x[i])

for x in [2,6,8,5,5]:
    for y in range(1,5):
        print(x,y)
##executes 20 times

x = 60

if x<100:
    grade = 'a'
elif x<90:
    grade = 'b'
elif x<80:
    grade = 'c'
else:
    grade = 'd'
print(grade)

s = "fur"
for i in ["deer", "horse", "dog"]:
    s=i+s
    print(s)

p = 1
k = 1
while k <= 5:
    p = p*k
    print(p)
    k = k+2
print("done")

if x == 0:
    print('Zero')
if (x%3)==0:
    print('Mult3')
if not((x==0) or ((x%3)==0)):
    print('not mult3')

def Simple(x):
    if x ==1:
        return("one")
    elif x==2:
        return("two")
    elif x==3:
        return("three")
    else:
        return(None)
assertEqual(Simple(1),1)
assertEqual(Simple(5),None)

def main():
    inp = input("Enter an integer 1 through 4:")
    while int(inp) != 4:
        if int(inp) == 1:
            print(Simple(1))
            inp = input('new choice:')
        elif int(inp) == 2:
            print(Simple(2))
            inp = input('new choice:')
        elif int(inp) == 3:
            print(Simple(3))
            inp = input('new choice:')
        else:
            inp = input("invalid choice try again:") 
    if int(inp) == 4:
        print('Goodbye')
main()
    
            
        
