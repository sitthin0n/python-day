hours = float(input("Enter working hours in a week: "))
pay_rate = float(input("Enter pay rate per hour: "))

if hours <= 40:
    gross_pay = hours * pay_rate
else:
    gross_pay = 40 * pay_rate + (hours - 40) * pay_rate * 1.5
print("Gross pay: $", format(gross_pay, '.2f'))