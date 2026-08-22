annual_salary=float(input("Please enter your annual salary: "))
total_cost=1000000
semi_annual_raise=0.07
high_rate=1.0
low_rate=0.0
month=36

money_rightnow=0
step=0

max_savings = 0.0
annual_salary_test = annual_salary
for month in range(1, 37):
    max_savings = max_savings * (1 + 0.04/12) + (annual_salary_test / 12) * 1.0
    if month % 6 == 0:
        annual_salary_test = annual_salary_test * (1 + 0.07)
if max_savings < 250000 - 100:
    print("It is not possible to pay the down payment in three years.")

    exit()


while money_rightnow>total_cost*0.25+100 or money_rightnow<total_cost*0.25-100:
    guess_rate=(high_rate+low_rate)/2
    step+=1
    money_rightnow=0
    annual_salary_test=annual_salary
    for month in range(1,month+1):
        money_rightnow=money_rightnow*(1+0.04/12)+annual_salary_test/12*guess_rate
        if month%6==0:
            annual_salary_test=annual_salary_test*(1+semi_annual_raise)
    if money_rightnow>total_cost*0.25+100:
        high_rate=guess_rate
    elif money_rightnow<total_cost*0.25-100 :
        low_rate=guess_rate

print("Best savings rate:", guess_rate) 
print("Steps in bisection search:", step)
