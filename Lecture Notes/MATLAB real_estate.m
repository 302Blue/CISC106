years = 1988:1994
years =
        1988        1989        1990        1991        1992        1993        1994
sales_M = [127 130 136 145 158 178 211]
sales_M =
   127   130   136   145   158   178   211
sales_B = [137, 130, 172, 204, 178, 158, 141]
sales_B =
   137   130   172   204   178   158   141
plot(years, sales_M, years, sales_B)
hold off
plot(years, sales_M, years, sales_B)

% Try to use a bar plot
bar(sales_M)
bar(years, sales_M)
hold on
bar(years, sales_B)
hold off

% It turns out we need to create a 2D array of the sales figures.
sales = [sales_M; sales_B]
sales =
   127   130   136   145   158   178   211
   137   130   172   204   178   158   141
bar(sales)

% We need to transpose the sales array because the rows correspond to categories, and
% we want the years to be the categories, not the cities.
sales'
ans =
   127   137
   130   130
   136   172
   145   204
   158   178
   178   158
   211   141
bar(years, sales')

legend ('City M', 'City B')
legend ('City M', 'City B', 'Location', 'best')
legend ('City M', 'City B', 'Location', 'northwest')

diary 05-09-16
