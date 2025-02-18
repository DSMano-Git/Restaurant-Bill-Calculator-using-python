print("Welcome to the Bill Calculator")

# Get the total bill, tip percentage, and number of people
total_bill = float(input("Enter the total bill amount: "))
tip_percentage = int(input("Enter the Percentage of tip you can give: 10, 12, or 15: "))
people = int(input("Enter the number of people you can share the billing: "))

#tip calculation
tip = (tip_percentage/100)*total_bill

#Total amount to be paid
total_bill = total_bill + tip

#amount per person
amount_per_person = total_bill/people

# Print the result
print(f"Total bill (including tip): {total_bill:.2f}")
print(f"Each person has to pay: {amount_per_person:.2f}")
