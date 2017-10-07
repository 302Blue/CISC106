function area_estimate = mc_area_estimator(num_darts)
% Use the Monte Carlo method to estimate the area of a
% rectangle with an actual area of 0.5.
% Parameters:
%   num_darts - number of Monte Carlo trials
% Variables:
%   darts_in_rectangle - count of darts that hit rectangle
%   y - y-coordinate of each dart that is thrown

% initialize counter
darts_in_rectangle = 0;

% Throw num_darts darts
for dart = 1:num_darts
    % pick random dart location
    % no need to pick an x location for this problem.
    y = rand;
    
    % check if dart is in rectangle
    if y <= 0.5
        darts_in_rectangle = darts_in_rectangle + 1;
    end
end

% Calculate and return area estimate
area_estimate = darts_in_rectangle / num_darts;

end

