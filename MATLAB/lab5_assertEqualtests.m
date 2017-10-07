%Andrew Baldwin and Samuel Cory

%%%Testing to make sure that the compute_circle_area 
% function is working correctly.
assertEqual(compute_circle_area(5),78.5398)
assertEqual(compute_circle_area(0),0)
assertEqual(compute_circle_area(8),201.0619)
assertEqual(compute_circle_area(3.14),30.9748)
% lab5_assertEqualtests.m: line 5: SUCCESS: assertEqual(compute_circle_area(5),78.5398)
% lab5_assertEqualtests.m: line 6: SUCCESS: assertEqual(compute_circle_area(0),0)
% lab5_assertEqualtests.m: line 7: SUCCESS: assertEqual(compute_circle_area(8),201.0619)
% lab5_assertEqualtests.m: line 8: SUCCESS: assertEqual(compute_circle_area(3.14),30.9748)

%%%Testing to make sure that compute_cylinder_volume
% is working correctly.
assertEqual(compute_cylinder_volume(0,0),0)
assertEqual(compute_cylinder_volume(1,3.14),30.9748)
assertEqual(compute_cylinder_volume(5,8),1005.3096)
assertEqual(compute_cylinder_volume(4,2),50.2654)
% lab5_assertEqualtests.m: line 12: SUCCESS: assertEqual(compute_cylinder_volume(0,0),0)
% lab5_assertEqualtests.m: line 13: SUCCESS: assertEqual(compute_cylinder_volume(1,3.14),30.9748)
% lab5_assertEqualtests.m: line 14: SUCCESS: assertEqual(compute_cylinder_volume(5,8),1005.3096)
% lab5_assertEqualtests.m: line 15: SUCCESS: assertEqual(compute_cylinder_volume(4,2),50.2654)

%%%Testing that sum_odd_ints is working correctly
assertEqual(sum_odd_ints(2,4),3)
assertEqual(sum_odd_ints(-3,10),21)
assertEqual(sum_odd_ints(3,7),15)
assertEqual(sum_odd_ints(3,8),15)
assertEqual(sum_odd_ints(1,5),9)
% lab5_assertEqualtests.m: line 18: SUCCESS: assertEqual(sum_odd_ints(2,4),3)
% lab5_assertEqualtests.m: line 19: SUCCESS: assertEqual(sum_odd_ints(-3,10),21)
% lab5_assertEqualtests.m: line 20: SUCCESS: assertEqual(sum_odd_ints(3,7),15)
% lab5_assertEqualtests.m: line 21: SUCCESS: assertEqual(sum_odd_ints(3,8),15)
% lab5_assertEqualtests.m: line 22: SUCCESS: assertEqual(sum_odd_ints(1,5),9)

%%%Testing to make sure linear search is working
assertEqual(linear_search(['x', 'e', 'w', 'q', 'z', 'r'], 'z'), 5)
assertEqual(linear_search([4, 7, 1, 8, 3, 0, 2, 9, 6], 7), 2)
assertEqual(linear_search([4, 7, 1, 8, 3, 0, 2, 9, 6], 4), 1)
assertEqual(linear_search([4, 7, 1, 8, 3, 0, 2, 9, 6], -7), 0)
assertEqual(linear_search([4, 7, 1, 8, 3, 0, 2, 9, 6], 5), 0)
% lab5_assertEqualtests.m: line 25: SUCCESS: assertEqual(linear_search(['x', 'e', 'w', 'q', 'z', 'r'], 'z'), 5)
% lab5_assertEqualtests.m: line 26: SUCCESS: assertEqual(linear_search([4, 7, 1, 8, 3, 0, 2, 9, 6], 7), 2)
% lab5_assertEqualtests.m: line 27: SUCCESS: assertEqual(linear_search([4, 7, 1, 8, 3, 0, 2, 9, 6], 4), 1)
% lab5_assertEqualtests.m: line 28: SUCCESS: assertEqual(linear_search([4, 7, 1, 8, 3, 0, 2, 9, 6], -7), 0)
% lab5_assertEqualtests.m: line 29: SUCCESS: assertEqual(linear_search([4, 7, 1, 8, 3, 0, 2, 9, 6], 5), 0)
