annual_salary=float(input("Firstly, please enter your annual salary: "))
portion_save=float(input("Now, please enter the percent of your salary to save: "))
total_cost=float(input("Besides, please enter the price of your dream house: "))
semi_annual_raise=float(input("Finally, please enter the semi-annual raise: "))

money_rightnow=0
month=0

while money_rightnow<total_cost*0.25:
    month+=1

    money_rightnow=money_rightnow*(1+0.04/12)+annual_salary/12*portion_save

    if month%6==0:
        annual_salary=annual_salary*(1+semi_annual_raise)

print("Number of months:", month)
