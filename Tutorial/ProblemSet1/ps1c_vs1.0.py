total_cost=1000000   #define the arguments
current_savings=0

r=0.04
semi_annual_raise=0.07
portion_down_payment=0.25

high_rate=10000
low_rate=0
decimal=10000

months=36
total_month_a_year=12
half_month_a_year=6

error=100

annual_salary=float(input("Please enter your annual salary: "))     #ask the user to input the annual salary

step=0

annual_salary_test = annual_salary

def rate_saving(savings, r, total_month_year):
    return savings * (r / total_month_year)

def transfer_saving(annual_salary_test, total_month_a_year, rate):
    return annual_salary_test / total_month_a_year * (rate / decimal)

def saving_formula(savings, r, total_month_a_year, annual_salary_test, rate):
    # savings += (savings * (r / total_month_a_year)) + (annual_salary_test / total_month_a_year * (rate / decimal))
    savings += rate_saving(savings, r, total_month_a_year) + transfer_saving(annual_salary_test, total_month_a_year, rate)
    return savings

def calculate_the_savings(annual_salary_test, rate, months, r, total_month_a_year, half_month_a_year, semi_annual_raise, savings):
    # max_savings = 0.0
    for month in range(1, months+1):
        # savings += (savings * (r / total_month_a_year)) + (annual_salary_test / total_month_a_year * (high_rate / decimal))
        savings = saving_formula(savings, r, total_month_a_year, annual_salary_test, rate)
        if month % half_month_a_year == 0:
            annual_salary_test *= (1 + semi_annual_raise)
    return savings 

# Determine the lowest salary for the house
max_savings = 0.0

max_savings = calculate_the_savings(annual_salary_test, high_rate, months, r, total_month_a_year, half_month_a_year, semi_annual_raise, max_savings)

if max_savings < total_cost*portion_down_payment - error:
    print("It is not possible to pay the down payment in three years.")
    exit()

# Determine the minimum rate for buying the house
while ((current_savings>total_cost*portion_down_payment+error) or (current_savings<total_cost*portion_down_payment-error)):
    current_rate=(high_rate+low_rate) // 2

    step+=1

    current_savings=0

    annual_salary_test=annual_salary

    current_savings = calculate_the_savings(annual_salary_test, current_rate, months, r, total_month_a_year, half_month_a_year, semi_annual_raise, current_savings)

    if current_savings > total_cost * portion_down_payment + error:
        high_rate=current_rate

    elif current_savings < total_cost * portion_down_payment - error:
        low_rate=current_rate

print("Best savings rate:", current_rate / decimal)

print("Steps in bisection search:", step)