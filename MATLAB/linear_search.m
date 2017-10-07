%Andrew Baldwin and Samuel Cory
function [Index] = linear_search(values,target)
%This function searches for the occurence of "target" in
%the "values" list. If found the index of target is 
%returned, if not 0 is returned.
%Parameters:
    %values (list)
    %target (any)
%Returns:
    %Index (int)
    %0 (int)
%Looping through elements in Values list
for x = 1:length(values)
    %Looking for match to target
    if values(x) == target
        Index = x;
        return
    end
end
%For when a match was not found
Index = 0;
return
end

