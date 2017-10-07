% scalar multiplication and addition
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

% matrix multiplication
x = [1 2 3]
x =
     1     2     3
A * x
{Error using <a href="matlab:matlab.internal.language.introspective.errorDocCallback('mtimes')" style="font-weight:bold"> * </a>
Inner matrix dimensions must agree.} 
A * x'
ans =
    14
    32
    53
A * B
ans =
     5     8    14
    14    20    32
    23    34    53
I = eye(3)
I =
     1     0     0
     0     1     0
     0     0     1
A * I
ans =
     1     2     3
     4     5     6
     7     8    10
I * A
ans =
     1     2     3
     4     5     6
     7     8    10

% element-wise multiplication
x = 1:3
x =
     1     2     3
y = 4:6
y =
     4     5     6
z = x + y
z =
     5     7     9
z = y - x
z =
     3     3     3
x = 1:10
x =
     1     2     3     4     5     6     7     8     9    10
x * x
{Error using <a href="matlab:matlab.internal.language.introspective.errorDocCallback('mtimes')" style="font-weight:bold"> * </a>
Inner matrix dimensions must agree.} 
x .* x
ans =
     1     4     9    16    25    36    49    64    81   100
x .^ 2
ans =
     1     4     9    16    25    36    49    64    81   100
x .^ x
ans =
   1.0e+10 *
  Columns 1 through 9
    0.0000    0.0000    0.0000    0.0000    0.0000    0.0000    0.0001    0.0017    0.0387
  Column 10
    1.0000

% alternate display formats
format shortEng
x .^ x
ans =
  Columns 1 through 6
     1.0000e+000     4.0000e+000    27.0000e+000   256.0000e+000     3.1250e+003    46.6560e+003
  Columns 7 through 10
   823.5430e+003    16.7772e+006   387.4205e+006    10.0000e+009
format lengEng
{Error using <a href="matlab:matlab.internal.language.introspective.errorDocCallback('format')" style="font-weight:bold">format</a>
Unknown command option.} 
format longEng
x .^ x
ans =
  Columns 1 through 3
    1.00000000000000e+000    4.00000000000000e+000    27.0000000000000e+000
  Columns 4 through 6
    256.000000000000e+000    3.12500000000000e+003    46.6560000000000e+003
  Columns 7 through 9
    823.543000000000e+003    16.7772160000000e+006    387.420489000000e+006
  Column 10
    10.0000000000000e+009
format long
x .^ x
ans =
   1.0e+10 *
  Columns 1 through 4
   0.000000000100000   0.000000000400000   0.000000002700000   0.000000025600000
  Columns 5 through 8
   0.000000312500000   0.000004665600000   0.000082354300000   0.001677721600000
  Columns 9 through 10
   0.038742048900000   1.000000000000000
format short
x .^ x
ans =
   1.0e+10 *
  Columns 1 through 9
    0.0000    0.0000    0.0000    0.0000    0.0000    0.0000    0.0001    0.0017    0.0387
  Column 10
    1.0000

% The colon operator allows the use of float values
x = 0:0.1:1
x =
  Columns 1 through 9
         0    0.1000    0.2000    0.3000    0.4000    0.5000    0.6000    0.7000    0.8000
  Columns 10 through 11
    0.9000    1.0000
x = 0.1: 0.01: 0.3
x =
  Columns 1 through 9
    0.1000    0.1100    0.1200    0.1300    0.1400    0.1500    0.1600    0.1700    0.1800
  Columns 10 through 18
    0.1900    0.2000    0.2100    0.2200    0.2300    0.2400    0.2500    0.2600    0.2700
  Columns 19 through 21
    0.2800    0.2900    0.3000
x = 0:0.01:10
x =
  Columns 1 through 9
         0    0.0100    0.0200    0.0300    0.0400    0.0500    0.0600    0.0700    0.0800
  Columns 10 through 18
    0.0900    0.1000    0.1100    0.1200    0.1300    0.1400    0.1500    0.1600    0.1700
  Columns 19 through 27
    0.1800    0.1900    0.2000    0.2100    0.2200    0.2300    0.2400    0.2500    0.2600
  Columns 28 through 36
    0.2700    0.2800    0.2900    0.3000    0.3100    0.3200    0.3300    0.3400    0.3500
  Columns 37 through 45
    0.3600    0.3700    0.3800    0.3900    0.4000    0.4100    0.4200    0.4300    0.4400
  Columns 46 through 54
    0.4500    0.4600    0.4700    0.4800    0.4900    0.5000    0.5100    0.5200    0.5300
  Columns 55 through 63
    0.5400    0.5500    0.5600    0.5700    0.5800    0.5900    0.6000    0.6100    0.6200
  Columns 64 through 72
    0.6300    0.6400    0.6500    0.6600    0.6700    0.6800    0.6900    0.7000    0.7100
  Columns 73 through 81
    0.7200    0.7300    0.7400    0.7500    0.7600    0.7700    0.7800    0.7900    0.8000
  Columns 82 through 90
    0.8100    0.8200    0.8300    0.8400    0.8500    0.8600    0.8700    0.8800    0.8900
  Columns 91 through 99
    0.9000    0.9100    0.9200    0.9300    0.9400    0.9500    0.9600    0.9700    0.9800
  Columns 100 through 108
    0.9900    1.0000    1.0100    1.0200    1.0300    1.0400    1.0500    1.0600    1.0700
  Columns 109 through 117
    1.0800    1.0900    1.1000    1.1100    1.1200    1.1300    1.1400    1.1500    1.1600
  Columns 118 through 126
    1.1700    1.1800    1.1900    1.2000    1.2100    1.2200    1.2300    1.2400    1.2500
  Columns 127 through 135
    1.2600    1.2700    1.2800    1.2900    1.3000    1.3100    1.3200    1.3300    1.3400
  Columns 136 through 144
    1.3500    1.3600    1.3700    1.3800    1.3900    1.4000    1.4100    1.4200    1.4300
  Columns 145 through 153
    1.4400    1.4500    1.4600    1.4700    1.4800    1.4900    1.5000    1.5100    1.5200
  Columns 154 through 162
    1.5300    1.5400    1.5500    1.5600    1.5700    1.5800    1.5900    1.6000    1.6100
  Columns 163 through 171
    1.6200    1.6300    1.6400    1.6500    1.6600    1.6700    1.6800    1.6900    1.7000
  Columns 172 through 180
    1.7100    1.7200    1.7300    1.7400    1.7500    1.7600    1.7700    1.7800    1.7900
  Columns 181 through 189
    1.8000    1.8100    1.8200    1.8300    1.8400    1.8500    1.8600    1.8700    1.8800
  Columns 190 through 198
    1.8900    1.9000    1.9100    1.9200    1.9300    1.9400    1.9500    1.9600    1.9700
  Columns 199 through 207
    1.9800    1.9900    2.0000    2.0100    2.0200    2.0300    2.0400    2.0500    2.0600
  Columns 208 through 216
    2.0700    2.0800    2.0900    2.1000    2.1100    2.1200    2.1300    2.1400    2.1500
  Columns 217 through 225
    2.1600    2.1700    2.1800    2.1900    2.2000    2.2100    2.2200    2.2300    2.2400
  Columns 226 through 234
    2.2500    2.2600    2.2700    2.2800    2.2900    2.3000    2.3100    2.3200    2.3300
  Columns 235 through 243
    2.3400    2.3500    2.3600    2.3700    2.3800    2.3900    2.4000    2.4100    2.4200
  Columns 244 through 252
    2.4300    2.4400    2.4500    2.4600    2.4700    2.4800    2.4900    2.5000    2.5100
  Columns 253 through 261
    2.5200    2.5300    2.5400    2.5500    2.5600    2.5700    2.5800    2.5900    2.6000
  Columns 262 through 270
    2.6100    2.6200    2.6300    2.6400    2.6500    2.6600    2.6700    2.6800    2.6900
  Columns 271 through 279
    2.7000    2.7100    2.7200    2.7300    2.7400    2.7500    2.7600    2.7700    2.7800
  Columns 280 through 288
    2.7900    2.8000    2.8100    2.8200    2.8300    2.8400    2.8500    2.8600    2.8700
  Columns 289 through 297
    2.8800    2.8900    2.9000    2.9100    2.9200    2.9300    2.9400    2.9500    2.9600
  Columns 298 through 306
    2.9700    2.9800    2.9900    3.0000    3.0100    3.0200    3.0300    3.0400    3.0500
  Columns 307 through 315
    3.0600    3.0700    3.0800    3.0900    3.1000    3.1100    3.1200    3.1300    3.1400
  Columns 316 through 324
    3.1500    3.1600    3.1700    3.1800    3.1900    3.2000    3.2100    3.2200    3.2300
  Columns 325 through 333
    3.2400    3.2500    3.2600    3.2700    3.2800    3.2900    3.3000    3.3100    3.3200
  Columns 334 through 342
    3.3300    3.3400    3.3500    3.3600    3.3700    3.3800    3.3900    3.4000    3.4100
  Columns 343 through 351
    3.4200    3.4300    3.4400    3.4500    3.4600    3.4700    3.4800    3.4900    3.5000
  Columns 352 through 360
    3.5100    3.5200    3.5300    3.5400    3.5500    3.5600    3.5700    3.5800    3.5900
  Columns 361 through 369
    3.6000    3.6100    3.6200    3.6300    3.6400    3.6500    3.6600    3.6700    3.6800
  Columns 370 through 378
    3.6900    3.7000    3.7100    3.7200    3.7300    3.7400    3.7500    3.7600    3.7700
  Columns 379 through 387
    3.7800    3.7900    3.8000    3.8100    3.8200    3.8300    3.8400    3.8500    3.8600
  Columns 388 through 396
    3.8700    3.8800    3.8900    3.9000    3.9100    3.9200    3.9300    3.9400    3.9500
  Columns 397 through 405
    3.9600    3.9700    3.9800    3.9900    4.0000    4.0100    4.0200    4.0300    4.0400
  Columns 406 through 414
    4.0500    4.0600    4.0700    4.0800    4.0900    4.1000    4.1100    4.1200    4.1300
  Columns 415 through 423
    4.1400    4.1500    4.1600    4.1700    4.1800    4.1900    4.2000    4.2100    4.2200
  Columns 424 through 432
    4.2300    4.2400    4.2500    4.2600    4.2700    4.2800    4.2900    4.3000    4.3100
  Columns 433 through 441
    4.3200    4.3300    4.3400    4.3500    4.3600    4.3700    4.3800    4.3900    4.4000
  Columns 442 through 450
    4.4100    4.4200    4.4300    4.4400    4.4500    4.4600    4.4700    4.4800    4.4900
  Columns 451 through 459
    4.5000    4.5100    4.5200    4.5300    4.5400    4.5500    4.5600    4.5700    4.5800
  Columns 460 through 468
    4.5900    4.6000    4.6100    4.6200    4.6300    4.6400    4.6500    4.6600    4.6700
  Columns 469 through 477
    4.6800    4.6900    4.7000    4.7100    4.7200    4.7300    4.7400    4.7500    4.7600
  Columns 478 through 486
    4.7700    4.7800    4.7900    4.8000    4.8100    4.8200    4.8300    4.8400    4.8500
  Columns 487 through 495
    4.8600    4.8700    4.8800    4.8900    4.9000    4.9100    4.9200    4.9300    4.9400
  Columns 496 through 504
    4.9500    4.9600    4.9700    4.9800    4.9900    5.0000    5.0100    5.0200    5.0300
  Columns 505 through 513
    5.0400    5.0500    5.0600    5.0700    5.0800    5.0900    5.1000    5.1100    5.1200
  Columns 514 through 522
    5.1300    5.1400    5.1500    5.1600    5.1700    5.1800    5.1900    5.2000    5.2100
  Columns 523 through 531
    5.2200    5.2300    5.2400    5.2500    5.2600    5.2700    5.2800    5.2900    5.3000
  Columns 532 through 540
    5.3100    5.3200    5.3300    5.3400    5.3500    5.3600    5.3700    5.3800    5.3900
  Columns 541 through 549
    5.4000    5.4100    5.4200    5.4300    5.4400    5.4500    5.4600    5.4700    5.4800
  Columns 550 through 558
    5.4900    5.5000    5.5100    5.5200    5.5300    5.5400    5.5500    5.5600    5.5700
  Columns 559 through 567
    5.5800    5.5900    5.6000    5.6100    5.6200    5.6300    5.6400    5.6500    5.6600
  Columns 568 through 576
    5.6700    5.6800    5.6900    5.7000    5.7100    5.7200    5.7300    5.7400    5.7500
  Columns 577 through 585
    5.7600    5.7700    5.7800    5.7900    5.8000    5.8100    5.8200    5.8300    5.8400
  Columns 586 through 594
    5.8500    5.8600    5.8700    5.8800    5.8900    5.9000    5.9100    5.9200    5.9300
  Columns 595 through 603
    5.9400    5.9500    5.9600    5.9700    5.9800    5.9900    6.0000    6.0100    6.0200
  Columns 604 through 612
    6.0300    6.0400    6.0500    6.0600    6.0700    6.0800    6.0900    6.1000    6.1100
  Columns 613 through 621
    6.1200    6.1300    6.1400    6.1500    6.1600    6.1700    6.1800    6.1900    6.2000
  Columns 622 through 630
    6.2100    6.2200    6.2300    6.2400    6.2500    6.2600    6.2700    6.2800    6.2900
  Columns 631 through 639
    6.3000    6.3100    6.3200    6.3300    6.3400    6.3500    6.3600    6.3700    6.3800
  Columns 640 through 648
    6.3900    6.4000    6.4100    6.4200    6.4300    6.4400    6.4500    6.4600    6.4700
  Columns 649 through 657
    6.4800    6.4900    6.5000    6.5100    6.5200    6.5300    6.5400    6.5500    6.5600
  Columns 658 through 666
    6.5700    6.5800    6.5900    6.6000    6.6100    6.6200    6.6300    6.6400    6.6500
  Columns 667 through 675
    6.6600    6.6700    6.6800    6.6900    6.7000    6.7100    6.7200    6.7300    6.7400
  Columns 676 through 684
    6.7500    6.7600    6.7700    6.7800    6.7900    6.8000    6.8100    6.8200    6.8300
  Columns 685 through 693
    6.8400    6.8500    6.8600    6.8700    6.8800    6.8900    6.9000    6.9100    6.9200
  Columns 694 through 702
    6.9300    6.9400    6.9500    6.9600    6.9700    6.9800    6.9900    7.0000    7.0100
  Columns 703 through 711
    7.0200    7.0300    7.0400    7.0500    7.0600    7.0700    7.0800    7.0900    7.1000
  Columns 712 through 720
    7.1100    7.1200    7.1300    7.1400    7.1500    7.1600    7.1700    7.1800    7.1900
  Columns 721 through 729
    7.2000    7.2100    7.2200    7.2300    7.2400    7.2500    7.2600    7.2700    7.2800
  Columns 730 through 738
    7.2900    7.3000    7.3100    7.3200    7.3300    7.3400    7.3500    7.3600    7.3700
  Columns 739 through 747
    7.3800    7.3900    7.4000    7.4100    7.4200    7.4300    7.4400    7.4500    7.4600
  Columns 748 through 756
    7.4700    7.4800    7.4900    7.5000    7.5100    7.5200    7.5300    7.5400    7.5500
  Columns 757 through 765
    7.5600    7.5700    7.5800    7.5900    7.6000    7.6100    7.6200    7.6300    7.6400
  Columns 766 through 774
    7.6500    7.6600    7.6700    7.6800    7.6900    7.7000    7.7100    7.7200    7.7300
  Columns 775 through 783
    7.7400    7.7500    7.7600    7.7700    7.7800    7.7900    7.8000    7.8100    7.8200
  Columns 784 through 792
    7.8300    7.8400    7.8500    7.8600    7.8700    7.8800    7.8900    7.9000    7.9100
  Columns 793 through 801
    7.9200    7.9300    7.9400    7.9500    7.9600    7.9700    7.9800    7.9900    8.0000
  Columns 802 through 810
    8.0100    8.0200    8.0300    8.0400    8.0500    8.0600    8.0700    8.0800    8.0900
  Columns 811 through 819
    8.1000    8.1100    8.1200    8.1300    8.1400    8.1500    8.1600    8.1700    8.1800
  Columns 820 through 828
    8.1900    8.2000    8.2100    8.2200    8.2300    8.2400    8.2500    8.2600    8.2700
  Columns 829 through 837
    8.2800    8.2900    8.3000    8.3100    8.3200    8.3300    8.3400    8.3500    8.3600
  Columns 838 through 846
    8.3700    8.3800    8.3900    8.4000    8.4100    8.4200    8.4300    8.4400    8.4500
  Columns 847 through 855
    8.4600    8.4700    8.4800    8.4900    8.5000    8.5100    8.5200    8.5300    8.5400
  Columns 856 through 864
    8.5500    8.5600    8.5700    8.5800    8.5900    8.6000    8.6100    8.6200    8.6300
  Columns 865 through 873
    8.6400    8.6500    8.6600    8.6700    8.6800    8.6900    8.7000    8.7100    8.7200
  Columns 874 through 882
    8.7300    8.7400    8.7500    8.7600    8.7700    8.7800    8.7900    8.8000    8.8100
  Columns 883 through 891
    8.8200    8.8300    8.8400    8.8500    8.8600    8.8700    8.8800    8.8900    8.9000
  Columns 892 through 900
    8.9100    8.9200    8.9300    8.9400    8.9500    8.9600    8.9700    8.9800    8.9900
  Columns 901 through 909
    9.0000    9.0100    9.0200    9.0300    9.0400    9.0500    9.0600    9.0700    9.0800
  Columns 910 through 918
    9.0900    9.1000    9.1100    9.1200    9.1300    9.1400    9.1500    9.1600    9.1700
  Columns 919 through 927
    9.1800    9.1900    9.2000    9.2100    9.2200    9.2300    9.2400    9.2500    9.2600
  Columns 928 through 936
    9.2700    9.2800    9.2900    9.3000    9.3100    9.3200    9.3300    9.3400    9.3500
  Columns 937 through 945
    9.3600    9.3700    9.3800    9.3900    9.4000    9.4100    9.4200    9.4300    9.4400
  Columns 946 through 954
    9.4500    9.4600    9.4700    9.4800    9.4900    9.5000    9.5100    9.5200    9.5300
  Columns 955 through 963
    9.5400    9.5500    9.5600    9.5700    9.5800    9.5900    9.6000    9.6100    9.6200
  Columns 964 through 972
    9.6300    9.6400    9.6500    9.6600    9.6700    9.6800    9.6900    9.7000    9.7100
  Columns 973 through 981
    9.7200    9.7300    9.7400    9.7500    9.7600    9.7700    9.7800    9.7900    9.8000
  Columns 982 through 990
    9.8100    9.8200    9.8300    9.8400    9.8500    9.8600    9.8700    9.8800    9.8900
  Columns 991 through 999
    9.9000    9.9100    9.9200    9.9300    9.9400    9.9500    9.9600    9.9700    9.9800
  Columns 1000 through 1001
    9.9900   10.0000

% Adding a semicolon at the end of a command suppresses output to the command window
x = 0:0.01:10;
y = x .^ 3;
y(57)
ans =
    0.1756
y(1:10:101)
ans =
  Columns 1 through 9
         0    0.0010    0.0080    0.0270    0.0640    0.1250    0.2160    0.3430    0.5120
  Columns 10 through 11
    0.7290    1.0000

y(1:10:201)
ans =
  Columns 1 through 8
         0    0.0010    0.0080    0.0270    0.0640    0.1250    0.2160    0.3430
  Columns 9 through 16
    0.5120    0.7290    1.0000    1.3310    1.7280    2.1970    2.7440    3.3750
  Columns 17 through 21
    4.0960    4.9130    5.8320    6.8590    8.0000

% The diary command allows you to record everything that happens in the command window,
% in a text file. Use “diary <filename>” to record to a file.
% “diary off” stops recording
diary off

% “diary on” resumes recording to the most recently used diary file. If no diary file has been specified yet, the default diary name is “diary”.

% Writing functions in MATLAB
clc
convert_F_to_C(212)
celsius =
   100
ans =
   100
convert_F_to_C(212)
ans =
   100

% Be sure to use the semicolon to suppress output from commands inside a function.
convert_F_to_C(32)
ans =
     0

% using assertEqual in MATLAB
assertEqual(convert_F_to_C(348.8), 176)
Command Window: line 0: SUCCESS: Command Window

% put assertEqual() tests inside a script file, and then run the script.
tests_convert_F_to_C
tests_convert_F_to_C.m: line 2: SUCCESS: assertEqual(convert_F_to_C(348.8), 176)
tests_convert_F_to_C.m: line 3: SUCCESS: assertEqual(convert_F_to_C(212), 100)
tests_convert_F_to_C.m: line 4: SUCCESS: assertEqual(convert_F_to_C(32), 0)
tests_convert_F_to_C.m: line 5: SUCCESS: assertEqual(convert_F_to_C(-40), -40)
tests_convert_F_to_C
tests_convert_F_to_C.m: line 2: SUCCESS: assertEqual(convert_F_to_C(348.8), 176)
tests_convert_F_to_C.m: line 3: SUCCESS: assertEqual(convert_F_to_C(212), 100)
tests_convert_F_to_C.m: line 4: SUCCESS: assertEqual(convert_F_to_C(32), 0)
tests_convert_F_to_C.m: line 5: FAILURE: assertEqual(convert_F_to_C(-40), -41), 
		 actual return value: -40   asserted return value: -41

clc
% run the script file to test the filter_data function
tests_filter_data
input_data =
  Columns 1 through 8
   20.1000   18.2000   24.3000   16.1000   45.5000   42.3000   46.1000   43.8000
  Column 9
   44.4000
output_data =
   20.2000   20.7250   25.5000   37.3500   44.0500   44.5750   44.5250
count =
     7
filtered_data =
   20.2000
filtered_data =
   20.2000   20.7250
filtered_data =
   20.2000   20.7250   25.5000
filtered_data =
   20.2000   20.7250   25.5000   37.3500
filtered_data =
   20.2000   20.7250   25.5000   37.3500   44.0500
filtered_data =
   20.2000   20.7250   25.5000   37.3500   44.0500   44.5750
filtered_data =
   20.2000   20.7250   25.5000   37.3500   44.0500   44.5750   44.5250
tests_filter_data.m: line 5: SUCCESS: assertEqual(filter_data(input_data), output_data)

clc
% add semicolons to suppress output inside the function
tests_filter_data
input_data =
  Columns 1 through 8
   20.1000   18.2000   24.3000   16.1000   45.5000   42.3000   46.1000   43.8000
  Column 9
   44.4000
output_data =
   20.2000   20.7250   25.5000   37.3500   44.0500   44.5750   44.5250
tests_filter_data.m: line 5: SUCCESS: assertEqual(filter_data(input_data), output_data)

clc
% also need to suppress output inside the script
tests_filter_data
tests_filter_data.m: line 5: SUCCESS: assertEqual(filter_data(input_data), output_data)

clc
% plotting
% polynomials
x = -10:0.01:10;
y1 = x;
y2 = x .^ 2;
y3 = x .^ 3;
plot(x, y1, x, y2, x, y3)
plot(x, y1, 'ro-', x, y2, 'gs-.', x, y3, 'b*--')

plot(x, y1, 'r-', x, y2, 'g-.', x, y3, 'b--')
axis([-10 10 -100 100])
grid on
legend('y = x', 'y = x^2', 'y = x^3')
legend('y = x', 'y = x^2', 'y = x^3', 'Location', 'north')
legend('y = x', 'y = x^2', 'y = x^3', 'Location', 'southwest')
legend('y = x', 'y = x^2', 'y = x^3', 'Location', 'best')

% trigonometric functions
x = 0:0.01:10;
r = sin(2*pi*x);
plot(x, r)
axis([0 4 -10 10])
s = sin(2*pi*x) ./ (2*pi*x);
plot(x, r, x, s)
diary off