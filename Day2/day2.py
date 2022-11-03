def Borders ():
    print(30 * "=-")

Borders()
print("Tip Calculator")
Borders()

total_bill = float(input("What was the total bill ?\n"))
amount_of_people = int(input("How many people will split this bill ?\n"))
tip_amount = float(input("How much would you like to tip ? None, 5%, 10% or 15%\n"))

tip_amount_float = float((total_bill * tip_amount) / 100)
total_amount_bill_float = float(total_bill + tip_amount_float)

if (amount_of_people == 0 or amount_of_people == 1):
    print(f"Total bill is {round(total_amount_bill_float)}")
elif (amount_of_people >= 1):
    print(f"The total bill per person is {round(total_amount_bill_float / amount_of_people)}")


