clc
% Monte Carlo Method
get_num_darts
Enter number of Monte Carlo Trials: 50
num_darts =
    50
ans =
    50
get_num_darts

% Add semicolon to suppress output from calling get_num_darts()
Enter number of Monte Carlo Trials: 50
ans =
    50

% What happens if we enter text?
get_num_darts
Enter number of Monte Carlo Trials: fifty
{Error using <a href="matlab:matlab.internal.language.introspective.errorDocCallback('input')" style="font-weight:bold">input</a>
Undefined function or variable 'fifty'.
Error in <a href="matlab:matlab.internal.language.introspective.errorDocCallback('get_num_darts', '/Users/jon/Documents/MATLAB/get_num_darts.m', 9)" style="font-weight:bold">get_num_darts</a> (<a href="matlab: opentoline('/Users/jon/Documents/MATLAB/get_num_darts.m',9,0)">line 9</a>)
    num_darts = input('Enter number of Monte Carlo Trials: ');}

% What if we explicitly make the text a string, like this?
Enter number of Monte Carlo Trials: 'fifty'
ans =
fifty

% We can also modify the input() function call by adding ’s’ as a 2nd argument. This
% tells input to interpret the input as text.
get_num_darts
Enter number of Monte Carlo Trials: fifty
ans =
fifty
get_num_darts
Enter number of Monte Carlo Trials: 50
ans =
    50

% Let’s create a script called mc_pi_estimator. The script should plot a circle, ask
% the user how many darts to throw, throw dart at the circle, plotting them and
% counting how many darts land in the circle, and report the estimated value of Pi.
mc_pi_estimator
mc_pi_estimator
mc_pi_estimator
mc_pi_estimator
mc_pi_estimator
Enter number of Monte Carlo Trials: 50
mc_pi_estimator
Enter number of Monte Carlo Trials: 50
mc_pi_estimator
Enter number of Monte Carlo Trials: 500
mc_pi_estimator
Enter number of Monte Carlo Trials: 50
mc_pi_estimator
Enter number of Monte Carlo Trials: 1000
mc_pi_estimator
Enter number of Monte Carlo Trials: 50
mc_pi_estimator
Enter number of Monte Carlo Trials: 500
mc_pi_estimator
Enter number of Monte Carlo Trials: 1000
mc_pi_estimator
Enter number of Monte Carlo Trials: 1000
mc_pi_estimator
Enter number of Monte Carlo Trials: 50
mc_pi =
    2.5600
mc_pi_estimator
Enter number of Monte Carlo Trials: 100
mc_pi =
    3.1200
mc_pi_estimator
Enter number of Monte Carlo Trials: 500
mc_pi =
    3.1280
mc_pi_estimator
Enter number of Monte Carlo Trials: 1000
mc_pi =
    3.1720
mc_pi_estimator
Enter number of Monte Carlo Trials: 1000
mc_pi =
    6.3640
mc_pi_estimator
Enter number of Monte Carlo Trials: 1000
mc_pi =
    3.0240

% We can output the result along wit explanatory text.
mc_pi_estimator
Enter number of Monte Carlo Trials: 1000
Monte Carlo estimate of pi = 3.056

% We can comment out all the plotting since it’s just eye candy and has nothing to do
% with estimating Pi. This will allow the code to run _much_ faster.
mc_pi_estimator
Enter number of Monte Carlo Trials: 100000
Elapsed time is 0.012561 seconds.
Monte Carlo estimate of pi = 3.14
format long
mc_pi_estimator
Enter number of Monte Carlo Trials: 1000000
Elapsed time is 0.121820 seconds.
Monte Carlo estimate of pi = 3.142152
mc_pi_estimator
Enter number of Monte Carlo Trials: 100000000
Elapsed time is 11.571345 seconds.
Monte Carlo estimate of pi = 3.1417494
clc

% Gauss-Jordan elimination
A = [3 2 4; 1 3 2; 2 4 3]
A =
     3     2     4
     1     3     2
     2     4     3
y = [170; 140; 200]
y =
   170
   140
   200

% Form the augmented matrix
M = [A y]
M =
     3     2     4   170
     1     3     2   140
     2     4     3   200

% Work to make the 1st column look like the identity matrix. Start by modifying the
% value at M(1, 1) to be 1. This can be accomplished by dividing the first row of M
% by the value at M(1, 1), like this:
M(1, :) = M(1, :) / M(1, 1)
M =
    1.0000    0.6667    1.3333   56.6667
    1.0000    3.0000    2.0000  140.0000
    2.0000    4.0000    3.0000  200.0000

% Subtracting the 1st row from the 2nd row modifies the value at M(2, 1) to be 0.
M(2, :) = M(2, :) - M(1, :)
M =
    1.0000    0.6667    1.3333   56.6667
         0    2.3333    0.6667   83.3333
    2.0000    4.0000    3.0000  200.0000

% Let’s use the same approach to make the value at M(3, 1) 0. Start by converting the
% value at M(3, 1) to 1, and then subtract the 1st row from the 3rd row.
M(3, :) = M(3, :) / M(3, 1)
M =
    1.0000    0.6667    1.3333   56.6667
         0    2.3333    0.6667   83.3333
    1.0000    2.0000    1.5000  100.0000
M(3, :) = M(3, :) - M(1, :)
M =
    1.0000    0.6667    1.3333   56.6667
         0    2.3333    0.6667   83.3333
         0    1.3333    0.1667   43.3333

% The 1st column now matches the identity matrix. 
% Now we move down the diagonal to M(2, 2) and try to make everything in column 2 look
% like the identity matrix, from M(2, 2) downwards. Let’s start by making the value at
% M(2, 2) =1, by dividing the 2nd row by the value at M(2, 2)
M(2, :) = M(2, :) / M(2, 2)
M =
    1.0000    0.6667    1.3333   56.6667
         0    1.0000    0.2857   35.7143
         0    1.3333    0.1667   43.3333

% Next let’s modify the value at M(3, 2) to 1 by dividing the 3rd row by M(3, 2).
M(3, :) = M(3, :) / M(3, 2)
M =
    1.0000    0.6667    1.3333   56.6667
         0    1.0000    0.2857   35.7143
         0    1.0000    0.1250   32.5000

% Now we’ll subtract row 2 from row 3 so that the value at M(3, 2) becomes 0.
M(3, :) = M(3, :) - M(2, :)
M =
    1.0000    0.6667    1.3333   56.6667
         0    1.0000    0.2857   35.7143
         0         0   -0.1607   -3.2143

% Move down the diagonal again, to M(3, 3), and modify this value to 1, to match the
% identity matrix. Do this by dividing the 3rd row by M(3, 3)
M(3, :) = M(3, :) / M(3, 3)
M =
    1.0000    0.6667    1.3333   56.6667
         0    1.0000    0.2857   35.7143
         0         0    1.0000   20.0000

% On Monday we’ll look at how to modify the values above to diagonal to be all zeroes,
% which will complete solving the problem.
diary off
