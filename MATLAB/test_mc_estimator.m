%Andrew Baldwin and Samuel Cory
function [Correct_95] = test_mc_estimator(num_trials,num_darts)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
trial_outputs = [];
Correct_95 = 0;
for x = 1:num_trials
    trial_outputs = [trial_outputs mc_area_estimator(num_darts)];
end
test_area1 = .95 * .5;
test_area2 = .95 * -.5;
for x = trial_outputs
    if (x <= test_area1) and (x >= test_area2)
        Correct_95 = Correct_95 + 1;
    end
end
Correct_95 = Correct_95 / num_trials;
return
end


