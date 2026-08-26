# ====================================
# Declaration part: 
# In most cases, the declaration part is at the top of the code.
# Mind to separate the lines for readability.
# Mind the "magic numbers" in the code below, they are constants that are given in the problem description.
total_cost=1000000
current_savings=0

r=0.04
semi_annual_raise=0.07
portion_down_payment=0.25

# Mind the decimals of accuracy mentioned in the question.
high_rate=10000
low_rate=0
decimal=10000
# high_rate=1.0
# low_rate=0.0

months=36
total_month_a_year=12
half_month_a_year=6

error=100
# ====================================

annual_salary=float(input("Please enter your annual salary: "))

# ====================================
# Using the variable given in the declaration part (current_savings), we can calculate the down payment of the house.
# money_rightnow=0
# ====================================

step=0

max_savings = 0.0
annual_salary_test = annual_salary

# ====================================
# Mind the "magic numbers" in the code below, they are constants that are given in the problem description.
for month in range(1, months+1):
# for month in range(1, 37):
# ====================================

    # ====================================
    # Using the variable (high_rate) defined before.
    # The expression can be simplified into:
    max_savings += (max_savings * (r / total_month_a_year)) + (annual_salary_test / total_month_a_year * (high_rate / decimal))
    # max_savings = max_savings * (1 + 0.04/12) + (annual_salary_test / 12) * 1.0
    # ====================================

    # ====================================
    # Using the variable defined before. 
    if month % half_month_a_year == 0:
    # if month % 6 == 0:
    # ====================================

        # ====================================
        # Using the variable (semi_annual_raise) defined before.
        # The expression can be simplifed into:
        annual_salary_test *= (1 + semi_annual_raise)
        # annual_salary_test = annual_salary_test * (1 + 0.07)
        # ====================================

# ====================================
# The calculation is not shown.
if max_savings < total_cost*portion_down_payment - error:
# if max_savings < 250000 - 100:
# ====================================

    print("It is not possible to pay the down payment in three years.")
    exit()

# ====================================
# Using the variable defined before.
while ((current_savings>total_cost*portion_down_payment+error) or
                  (current_savings<total_cost*portion_down_payment-error)):
# while current_savings>total_cost*0.25+100 or current_savings<total_cost*0.25-100:
# ====================================

    # ====================================
    # Not a suitable vairable name, we may call it current_rate
    current_rate=(high_rate+low_rate) // 2
    # guess_rate=(high_rate+low_rate)/2
    # ====================================

    step+=1

    current_savings=0

    annual_salary_test=annual_salary

    for month in range(1,months+1):

        # ====================================
        # Using the variable defined before.
        # The expression can be simplifed into:
        current_savings += (current_savings * (r / total_month_a_year)) + ((annual_salary_test / total_month_a_year) * (current_rate / decimal))
        # current_savings=current_savings*(1+0.04/12)+annual_salary_test/12*guess_rate
        # ====================================

        # ====================================
        # Using the variable defined before. 
        if month % half_month_a_year == 0:
        # if month % 6 == 0:
        # ====================================

            # ====================================
            # The expression can be simplifed into:
            annual_salary_test *= (1 + semi_annual_raise)
            # annual_salary_test=annual_salary_test*(1+semi_annual_raise)
            # ====================================
    
    # ====================================
    # The calculation is not shown.
    if current_savings > total_cost * portion_down_payment + error:
    # if current_savings>total_cost*0.25+100:
    # ====================================

        # ====================================
        # Use the suitable name for the variable
        high_rate=current_rate
        # high_rate=guess_rate
        # ====================================

    # ====================================
    # The calculation is not shown.
    elif current_savings < total_cost * portion_down_payment - error:
    # elif current_savings<total_cost*0.25-100:
    # ====================================

        # ====================================
        # Use the suitable name for the variable
        low_rate=current_rate
        # low_rate=guess_rate
        # ====================================
    
    print("Current iteration: ", step, "; Current rate: ", current_rate)

# ====================================
# Use the suitable name for the variable
print("Best savings rate:", current_rate / decimal)
# print("Best savings rate:", guess_rate) 
# ====================================

print("Steps in bisection search:", step)
