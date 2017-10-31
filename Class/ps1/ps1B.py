from decimal import Decimal

annual_salary = Decimal(input('Enter your annual salary: '))
portion_saved_rate = Decimal(
    input('Enter the percent of your salary to save, as a decimal: '))
total_cost = Decimal(input('Enter the cost of your dream home: '))
semi_annual_raise = Decimal(
    input('Enter the semi­annual raise, as a decimal: '))

monthly_salary = annual_salary / 12
portion_saved = portion_saved_rate * monthly_salary

portion_down_payment = total_cost * Decimal(0.25)

current_savings = Decimal(0.0)
annual_rate = Decimal(0.04)

months = 0
while current_savings < portion_down_payment:
    months += 1
    current_savings += current_savings * annual_rate / 12
    current_savings += portion_saved

    if months % 6 == 0:
        annual_salary += annual_salary * semi_annual_raise
        monthly_salary = annual_salary / 12
        portion_saved = portion_saved_rate * monthly_salary

print('Number of months:', months)
