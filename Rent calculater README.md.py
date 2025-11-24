## Inputs we need from the user 
# Total rent 
# Total food ordered for snacking 
# Electricity units sepd 
# Charge per unit 
# Persons living in the flat/hostel

## Output 
# Total amount you've to pay is 

rent = int(input("Enter your hostel/flat rent = "))
food = int(("Enter total amount spent on food = "))
electricity_units = int(input("Enter total electricity units consumed = "))
charge_per_unit = int(input("Enter charge per unit of electricity = "))
total_electricity_bill = electricity_units * charge_per_unit
total_amount = rent + food + total_electricity_bill
print("Total amount you've to pay is =", total_amount)
