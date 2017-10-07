2% MATLAB basics
a = 5

a =

     5

b = 9

b =

     9

c = a * b

c =

    45

d = a ** b
 d = a ** b
        |
{Error: Unexpected MATLAB operator.
} 
d = a ^ b

d =

     1953125

d = b % a

d =

     9

d = mod(b, a)

d =

     4

d = rem(b, a)

d =

     4

d = b // a
 d = b // a
        |
{Error: Unexpected MATLAB operator.
} 
d = floor(b / a)

d =

     1

format compact

% creating arrays
x = [-1, 1, 3, 5]
x =
    -1     1     3     5

x = [1 2 3 4 5]
x =
     1     2     3     4     5

% indexing into an array - indices start at 1!
x = [1 3 5 7 9]
x =
     1     3     5     7     9
x(2)
ans =
     3
x(4)
ans =
     7
x(0)
{Subscript indices must either be real positive integers or logicals.} 


% creating arrays with the MATLAB colon operator
1:5
ans =
     1     2     3     4     5
1:10
ans =
     1     2     3     4     5     6     7     8     9    10

% start:step:stop, default step value is 1, and not default start or stop
x = 0:1:10
x =
     0     1     2     3     4     5     6     7     8     9    10
x = 0:5:20
x =
     0     5    10    15    20
x = 10:-3:1
x =
    10     7     4     1
x = 10:-3:0
x =
    10     7     4     1

% The stop value is included if it’s part of the sequence
x = 2:2:9
x =
     2     4     6     8
x = 2:2:6
x =
     2     4     6


% array sections
x = 10:-1:1
x =
    10     9     8     7     6     5     4     3     2     1
x(2)
ans =
     9
x(4)
ans =
     7
x(6)
ans =
     5
x([2, 4, 6])
ans =
     9     7     5
x([1 7 8])
ans =
    10     4     3

% sections using the colon operator
x(2:8)
ans =
     9     8     7     6     5     4     3
x(2:2:8)
ans =
     9     7     5     3
x(1:3:10)
ans =
    10     7     4     1

% concatenating arrays
x = 1:3
x =
     1     2     3
y = 4:6
y =
     4     5     6
z = [x y]
z =
     1     2     3     4     5     6
c = cat(2, x, y)
c =
     1     2     3     4     5     6

% size or length of an array
x = 1:10
x =
     1     2     3     4     5     6     7     8     9    10
length(x)
ans =
    10
size(x, 1)
ans =
     1
size(x, 2)
ans =
    10

% creating 2D arrays
x = [1 2; 3 4]
x =
     1     2
     3     4

y = [1 2 3; 4 5 6; 7 8 10]
y =
     1     2     3
     4     5     6
     7     8    10

x = 1:3
x =
     1     2     3
y = 4:6
y =
     4     5     6
z = [x; y]
z =
     1     2     3
     4     5     6
cat(1, x, y)
ans =
     1     2     3
     4     5     6
cat(2, x, y)
ans =
     1     2     3     4     5     6


% indexing and sectioning of 2D arrays
d = [1 2 3 4; 5 6 7 8; 9 10 11 12; 13 14 15 16]
d =
     1     2     3     4
     5     6     7     8
     9    10    11    12
    13    14    15    16

d(2, 3)
ans =
     7
d(4, 1)
ans =
    13

d(1:3, 3:4)
ans =
     3     4
     7     8
    11    12

d(1:2:4, 3:4)
ans =
     3     4
    11    12

d(1:3, :)
ans =
     1     2     3     4
     5     6     7     8
     9    10    11    12

% Methematical operations with arrays
% scalar product, dot product, transpose
x = 1:5
x =
     1     2     3     4     5
3 * x
ans =
     3     6     9    12    15
y = 1:2:9
y =
     1     3     5     7     9
dot(x, y)
ans =
    95

x
x =
     1     2     3     4     5
x'
ans =
     1
     2
     3
     4
     5

% matrix operations
x
x =
     1     2     3     4     5
x * x
{Error using <a href="matlab:matlab.internal.language.introspective.errorDocCallback('mtimes')" style="font-weight:bold"> * </a>
Inner matrix dimensions must agree.} 

x * x'
ans =
    55
x' * x
ans =
     1     2     3     4     5
     2     4     6     8    10
     3     6     9    12    15
     4     8    12    16    20
     5    10    15    20    25

% scalar multiplication and matrix addition
A = [1 2 3; 4 5 6; 7 8 10]
A =
     1     2     3
     4     5     6
     7     8    10
3 * A
ans =
     3     6     9
    12    15    18
    21    24    30
B = [1 2 1; 2 0 2; 0 2 3]
B =
     1     2     1
     2     0     2
     0     2     3
C = A + B
C =
     2     4     4
     6     5     8
     7    10    13
