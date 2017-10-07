%Andrew Baldwin and Samuel Cory
function [cylinder_volume] = compute_cylinder_volume(height,radius)
%Calculate the volume of a cylinder given its height and radius.
% Also calls the compute_circle_area function to help complete this.
% Parameters:
    %height (float)
    %radius (float)
%Returns:
    %cylinder_volume (float)
%Area = Pi*R^2*H
cylinder_volume = compute_circle_area(radius) * height;
end

