# Prompt user for hours and rate per hour
hours = input("Enter hours: ")
rate_per_hour = input("Enter rate per hour: ")

# Convert the input strings to numbers 
hours = float(hours)
rate_per_hour = float(rate_per_hour)

# Calculate the gross pay with overtime pay for hours above 40
if hours > 40: 
    regular_pay = 40 * rate_per_hour
    overtime_pay = (hours - 40) * rate_per_hour * 1.5
    gross_pay = regular_pay + overtime_pay
else: 
    gross_pay = hours * rate_per_hour
    
#Print the result
print(gross_pay)