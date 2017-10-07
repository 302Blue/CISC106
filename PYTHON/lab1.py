##Andrew Baldwin
#Lab1

#1) Personal Information
print( )
#This is printing a space.
print("Problem One")
#This is printing the problem number.
print('Andrew Baldwin')
#This function is diplaying my name.
print('115 Tuckahoe Lane, Hockessin Delaware, 19707')
#This function is displaying my full address.
print('302-743-7309')
#Thing function is displaying my phone number.
print('Undecided- Going into either CPEG or CISC')
#This function is displaying my college major.


#2) Sales Prediction
print( )
#This is printing a space.
print("Problem Two")
#This is printing the problem number.
Total_Sales = float(input("What is your companies' total sales this year?"))
#This function gets the user to input their total sales and then also converts
##that input into a float value for later calculations, then finally assigns 
###that to the Total_Sales variable.
Profit = Total_Sales * .23
#This function takes the float value and multipies it by .23 to get the 23%
##profit of the Total_Sales and then assigns all of that to the Profit variable.
print('Your projected profit this year will be $', format(Profit,'.2f'), sep="")
#This function then displays the calculated profit to two decimals with the sentence
##"Your projected profit this year will be before" it.


#3) Land Calculation
print( )
#This is printing a space.
print("Problem Three")
#This is printing the problem number.
Land = float(input('How many square feet are there in the tract of land you are measuring?'))
#This line has the user input the amount of square feet in their land tand then changes
##that value to a float value while also assigning it to the Land variable.
Acres = Land / 43560
#This line takes the land variable and divides it by 43560, the amount of square feet
##in one acre, and then assigns that new amount to the variable Acres.
print("The land you are measuring has" , format(Acres, '.6f'), "acres in it")
#This function takes the amount of acres and displays it to 6 decimals by putting 
##the variable Acres in between "The land you are measuring has" and "acres in it".


#4) Total Purchase
print( )
#This is printing a space.
print("Problem Four")
#This is printing the problem number.
One = float(input("What is the price of your first item?"))
#This function asks the user for the price of their first item and converts 
##it to a float value while also assigning their input to a variable.
Two = float(input("What is the price of your second item?"))
#This function asks the user for the price of their second item and converts
## it to a float value while also assigning their input to a variable.
Three = float(input("What is the price of your third item?"))
#This function asks the user for the price of their third item and converts 
##it to a float value while also assigning their input to a variable.
Four = float(input("What is the price of your fourth item?"))
#This function asks the user for the price of their fourth item and converts 
##it to a float value while also assigning their input to a variable.
Five = float(input("What is the price of your fifth item?"))
#This function asks the user for the price of their fifth item and converts
## it to a float value while also assigning their input to a variable.
Sub = float(One + Two + Three + Four + Five)
#This function adds all of the items together and coverts the value to a float,
##and then assigns that value to the Sub variable.
print("Your subtotal is $", Sub, sep="")
#This line is printing the subtotal of their items with the sentence
##"Your subtotal is" before it.
print("The tax is .7%")
#This line is just telling them the amount of tax that there is.
Total = Sub + (Sub * .07)
#This is just applying the amount of tax to the subtotal and applying
##it to the variable Total.
Total = float(Total)
#Here, the Total is changed to a float value.
print("Therefore, your complete total is $", format(Total, '.2f'), sep="")
#Finally, this is printing their total to 2 decimals with the sentence
##"Therefore, your total is" before it.

#6) Sales Tax
print( )
#This is just printing a space.
print("Problem Six")
#This is printing the problem number.
Total = float(input("What is the total of your purchase?"))
#This function is getting the user to input the price of their purchase 
##and then converting that value to a float, and then finally assigning that
###value to a variable.
print("Your total is $", Total, sep="")
#This line is simply restating the user's total.
print("There is a state tax of 5%")
#This line is stating the amount of state tax.
print("There is county tax of 2.5% aswell")
#This is stating the amount of county tax.
print("Therefore, your purchase has a total tax of 7.5%")
#This is just displaying the two taxes combined.
Price = Total + (Total * .075)
#This function calculates the total cost and assigns it to the Price variable.
print("Your final purchase price is $", format(Price, '.2f'), sep="")
#This last line is displaying the final cost with two decimals.


#8) Tip, Tax, and Total
print( )
#This is just printing a space
print("Problem Eight")
#This is displaying the problem number
Meal = float(input("How much did your meal cost?"))
#This line asks the user how much their meal costs, converts that 
##to a float value, and then convert that to the Meal variable.
print("You have a 7% sales tax")
#This simply shows the user the amount of sales tax.
print("You are also giving a tip of 18%")
#This tells the user the amount of tip they are giving.
Price = Meal + ( Meal * .25)
#This function calculates the total price of the meal when the sales
##tax and tip are included.
print("Your final meal price is $", format(Price, '.2f'), sep="")
#This line shows the user their final meal price to two decimals.

#10) Ingredient Adjuster???
print( )
#This is creating a space
print("Problem 10")
#This line is displaying "Problem 10"
Cookies = float(input("How many cookies do you want to make today?"))
#This is assigning the Cookies variable to the user's amount of cookies and
##converting that amount to a float value.
Sugar = float((Cookies / 48) * 1.5)
#This line is calculating the amount of sugar needed per 48 cookies and 
##converting that amount to a float value for the variable Sugar
Butter = float((Cookies / 48) * 1)
#This line is calculating the amount of butter needed per 48 cookies
##and converting that amount to a float value for the variable Butter
Flour = float((Cookies / 48) * 2.75)
#This line is calculating the amount of flour needed per 48 cookies 
##and converting that amount to a float value for the variable Flour
print("You will need", format(Sugar, '.2f'), "cups of sugar")
#This is displaying the amount of sugar needed for the recipe
##to two decimal places
print("And also", format(Butter, '.2f'), "cups of butter")
#This is displaying the amount of butter needed for the recipe
##to two decimal places
print("and finally, you need", format(Flour, '.2f'), "cups of flour")
#This is displaying the amount of flour needed for the reciple
##to two decimal places

#11) Male and Female Percentages (Extra Credit)
print( )
#This line is creating a space
print("Problem Eleven")
#This function is displaying "Problem Eleven"
XX = float(input("How many females are there in your class?"))
#This function is asking the user for the number of females, converting
##that number to a float value, then assigning that variable to XX
XY = float(input("How many males are there in your class?"))
#This function is asking the user for the number of females, converting
##that number to a float value, then assigning that variable to XY
Total = XX + XY
#This is taking adding the XX and XY variables and assigning
##that value to the Total variable
Males = float(XY / Total)
#This function is assigning the Males variable to the ratio of males
##to the total, and making that ratio into a float value.
Females = float(XX / Total)
#This function is assigning the Females variable to the ratio of females
##to the total, and making that ratio into a float value.
print("The percentage of females in the class is ", format(Females * 100, '.2f'),"%", sep="")
#The line is displaying the amount of females in the class as a percentage.
print("The percentage of males in the class is ", format(Males * 100, '.2f'),"%", sep="")
#This last line is displaying the number of males in the class as a percentage too













































##WRX##
