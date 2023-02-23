# Create a tip calculator that lets each dinner guest know what their total contribution is AFTER tip
# Title for print screen
print('Welcome to the tip calculator.')

# Input for bill cost
bill = input('What was the total bill?\n')
bill_amount = float(bill)

# Input for tip amount
tip = input('What percentage tip would you like to give?\n')
tip_amount = round(bill_amount * (int(tip)/100), 2)

total_amount = tip_amount + bill_amount

# Input for number of people eating
num_of_people = input('How many people are eating?\n')

amount_per_person = round(total_amount/int(num_of_people), 2)

# Print result
print(f"Each person should pay: ${amount_per_person}")