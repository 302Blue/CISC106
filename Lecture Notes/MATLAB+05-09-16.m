format compact
clc

% compare linear and binary searches
n = 10:100:1000000;
linear = n / 2;
plot(n, linear)
binary = log2(n);
plot(n, binary)
hold on
plot(n, linear)

% Put commands in a script - search_comparisons
search_comparisons
search_comparisons
search_comparisons

% focus on region of plot near the origin
axis([0 1000000 0 100])
axis([0 10000 0 100])
axis([0 1000 0 100])
axis([0 1000 0 20])
search_comparisons
search_comparisons
search_comparisons
search_comparisons
search_comparisons

% The print command allows you to save a figure programatically.
print -dpng 'Comparisons.png'
clc
diary off

% This is where we switched to the real_estate diary and then back again.

clc
% linspace() function - ensures the array begins and ends on exactly the values specified
% creating an array with the concatenation operator
x = [1 2 3 4 5]
x =
     1     2     3     4     5
% creating an array with the colon operator
x = 1:5
x =
     1     2     3     4     5
% creating an array with the linspace() function
x = linspace(1, 5, 5)
x =
     1     2     3     4     5

% Note that this array doesn’t end exactly on pi
x = 0:0.1:pi
x =
  Columns 1 through 8
         0    0.1000    0.2000    0.3000    0.4000    0.5000    0.6000    0.7000
  Columns 9 through 16
    0.8000    0.9000    1.0000    1.1000    1.2000    1.3000    1.4000    1.5000
  Columns 17 through 24
    1.6000    1.7000    1.8000    1.9000    2.0000    2.1000    2.2000    2.3000
  Columns 25 through 32
    2.4000    2.5000    2.6000    2.7000    2.8000    2.9000    3.0000    3.1000

% Since x doesn’t end on pi, the plot stop short of pi.
plot(x, sin(x))
x = linspace(1, pi, 32)
x =
  Columns 1 through 8
    1.0000    1.0691    1.1382    1.2073    1.2763    1.3454    1.4145    1.4836
  Columns 9 through 16
    1.5527    1.6218    1.6908    1.7599    1.8290    1.8981    1.9672    2.0363
  Columns 17 through 24
    2.1053    2.1744    2.2435    2.3126    2.3817    2.4508    2.5198    2.5889
  Columns 25 through 32
    2.6580    2.7271    2.7962    2.8653    2.9343    3.0034    3.0725    3.1416
plot(x, sin(x))

% This ensures that the x array stop exactly on pi
x = linspace(0, pi, 32)
x =
  Columns 1 through 8
         0    0.1013    0.2027    0.3040    0.4054    0.5067    0.6081    0.7094
  Columns 9 through 16
    0.8107    0.9121    1.0134    1.1148    1.2161    1.3174    1.4188    1.5201
  Columns 17 through 24
    1.6215    1.7228    1.8242    1.9255    2.0268    2.1282    2.2295    2.3309
  Columns 25 through 32
    2.4322    2.5335    2.6349    2.7362    2.8376    2.9389    3.0403    3.1416

% Now the plot stops exactly at pi
plot(x, sin(x))

clc
% random numbers
% uniform random numbers in [0, 1]
rand
ans =
    0.8147
rand()
ans =
    0.9058
rand(1, 5)
ans =
    0.1270    0.9134    0.6324    0.0975    0.2785
rand(4, 4)
ans =
    0.5469    0.9706    0.1419    0.9595
    0.9575    0.9572    0.4218    0.6557
    0.9649    0.4854    0.9157    0.0357
    0.1576    0.8003    0.7922    0.8491
rand(3)
ans =
    0.9340    0.7431    0.1712
    0.6787    0.3922    0.7060
    0.7577    0.6555    0.0318

% uniform random integers in [1, N]
randi(10)
ans =
     3
randi(10)
ans =
     1
randi(10)
ans =
     1
randi(10)
ans =
     9
randi(10)
ans =
     7
randi(10, 1, 5)
ans =
     4    10     1     5     4
randi(10, 4)
ans =
     8     5     3     2
     8     7     7     5
     2     8     7    10
     5     8     2     4

% random normal distribution
randn()
ans =
    0.3714
randn(2, 6)
ans =
   -0.2256   -1.0891    0.5525    1.5442   -1.4916   -1.0616
    1.1174    0.0326    1.1006    0.0859   -0.7423    2.3505
randn(3)
ans =
   -0.6156    0.8886   -1.4224
    0.7481   -0.7648    0.4882
   -0.1924   -1.4023   -0.1774

% plot a histogram of random normal values
hist(randn(1, 10))
hist(randn(1, 100))
hist(randn(1, 1000))

% We can specify the number of bins
hist(randn(1, 1000), 50)
hist(randn(1, 100000), 50)
hist(randn(1, 10000000), 50)
hist(randn(1, 10000000), 500)
hist(randn(1, 100000000), 500)

% Timing code
% tic - starts the clock (or restarts the clock)
% toc - reports the elapsed time since the last tic

tic
toc
Elapsed time is 1.816553 seconds.
toc
Elapsed time is 4.391882 seconds.
toc
Elapsed time is 8.872009 seconds.
toc
Elapsed time is 13.671518 seconds.
tic
tic
toc
Elapsed time is 2.328054 seconds.
toc
Elapsed time is 5.527904 seconds.

clc
hist_timer
Elapsed time is 4.592910 seconds.
clc
diary off