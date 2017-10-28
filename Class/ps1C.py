from decimal import Decimal


semi_annual_raise = Decimal(0.07)
interest_rate = Decimal(0.04)
total_cost = Decimal(1000000)
down_payment = total_cost * 0.25

annual_salary = Decimal(input('Enter the starting salary: '))
monthly_salary = annual_salary / 12
