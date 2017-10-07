%Andrew Baldwin and Samuel Cory
function [Sum] = sum_odd_ints(start,stop)
%Returns the sums of all odd integers in between start and stop.
%Parameters:
    %start (int)
    %stop (int)
%Returns:
    %Sum (int)
%Set Sum accumulator to 0
Sum = 0;
%Creates the list specified in the parameters
Odd_list = start:stop;
%Loops through and sums only odd numbers
for x = Odd_list
    if mod(x,2) >= 1
        Sum = Sum + x;
    end
end  

end

