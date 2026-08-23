# ====================================
# Declaration part: 
# Mind the "magic numbers" in the code below, they are constants that are given in the problem description.
portion_down_payment=0.25
current_savings=0
r=0.04

total_month_a_year=12
# ====================================

annual_salary=float(input("Firstly, please enter your annual salary: "))
portion_save=float(input("Now, please enter the percent of your salary to save: "))
total_cost=float(input("At last, please enter the price of your dream house: "))

# ====================================
# Using the variable given in the declaration part (current_savings), we can calculate the down payment of the house.
# money_rightnow=0
# ====================================

month=0

# ====================================
# Using the variable defined before. 
while current_savings < total_cost * portion_down_payment:
# while money_rightnow<total_cost*0.25:
# ====================================

    month+=1

    # ====================================
    # Using the variable defined before.
    # The expression can be simplified into:
    current_savings += (current_savings * (r / total_month_a_year)) + ((annual_salary / total_month_a_year) * portion_save)
    # money_rightnow=money_rightnow*(1+0.04/12)+annual_salary/12*portion_save
    # ====================================

print("Number of months:", month)
