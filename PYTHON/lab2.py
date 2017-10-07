from cisc106_34 import assertEqual
def bill_amount(data, base_rate):
    if data <= 500:
        total_charge = base_rate*1
    elif data >= 500 and data <= 2500:
        total_charge = (base_rate*1.25) + ((data - 500) * .01)
    elif data >= 2500 and data <= 12500:
        total_charge = (base_rate*3.75) + ((data - 2500) * .025)
    else:
        total_charge = (base_rate*30)
    return(total_charge)

def time_calculator(seconds):
    Days = seconds // 86400
    Hours = (seconds % 86400) // 3600
    Mins = ((seconds % 86400) % 3600) // 60
    Secs = (((seconds % 86400) % 3600) % 60)
    print(seconds, "equals", Days, "days", Hours, "hours", Mins, "minutes and", Secs, "seconds")

def mortgage_approval(loan_amount, current_salary, account_balance, non_cash_assets, credit_score, last_name):
    '''
This function decides whether or not someone is eligible to get approved for a mortgage loan.
Parameters:
loan_amount (float) - This is how much money is being requested for the mortgage.
current_salary (float) - This is the person's current salary.
account_balance (float) - This is how much money the person's accounts are currently holding.
non_cash_assets (float) - This is the amount of non-cash assets the person currently has.
credit_score (int) - This is the person's credit score
last_name (str) - This is the person's last name.
Returns:
decision (str) - This is the answer to whether or not the person is eligible for the loan.
    '''
    if  (float(account_balance)) < (float(loan_amount) * .15):
        decision = "No"
    elif (int(credit_score)) < (590):
        decision = "No"
    elif (int(credit_score) >= (590) and int(credit_score) < (700)) and ((float(account_balance)) < (.25 * float(loan_amount))):
        decision = "No"
    elif (float(current_salary)) < ((1/3) * (float(loan_amount) - float(account_balance))):
        decision = "No"
    elif (str(last_name) == "Doe") and (float(non_cash_assets) < 750000):
        decision = "No"
    elif (float(account_balance)) > (float(loan_amount)):
        decision = "Yes"
    else:
        decision = "Maybe"
    return(decision)

assertEqual(mortgage_approval(100, 250, 5, 500, 600, "Hi"), 'No') #Testing account_balance < loan_amount * .15 when True
assertEqual(mortgage_approval(5, 250, 500, 500, 580, "Hi"), 'No')  #Testing credit_score < (590) when True
assertEqual(mortgage_approval(4000, 250, 500, 500, 600, "Hi"), 'No') #Testing (credit_score >= (590) and credit_score < (700))
                                                                   ##and (account_balance < (.25 * loan_amount)) when True
assertEqual(mortgage_approval(4000, 250, 500, 500, 600, "Hi"), 'No') #Testing current_salary <
                                                                   ##((1/3) * (loan_amount - account_balance)) when True
assertEqual(mortgage_approval(100, 250, 500, 500, 600, "Doe"), 'No') #Testing (last_name == "Doe") and
                                                                   ##(non_cash_assets < 750000) when True
assertEqual(mortgage_approval(5, 600, 500, 500, 600, "Hi"), 'Yes') #Testing account_balance > loan_amount when True
assertEqual(mortgage_approval(700, 600, 500, 500, 800, "Hi"), 'Maybe') #Testing else
assertEqual(mortgage_approval(700, 250, 175, 500, 600, "Hi"), 'Maybe') #Testing (credit_score >= (590) and credit_score < (700))
                                                                   ##and (account_balance >= (.25 * loan_amount)) when False
assertEqual(mortgage_approval(5, 250, 500, 800000, 600, "Doe"), 'Yes') #Testing (last_name == "Doe") and
                                                                   ##(non_cash_assets < 750000) when False





