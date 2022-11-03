def Borders ():
    print(30 * "=-")

Borders()
print("Tip Calculator")
Borders()

total_bill = input("What was the total bill ?\n")
amount_of_people = input("How many people will split this bill ?\n")
tip_amount = input("How much would you like to tip ? None, 5%, 10% or 15%\n")

total_bill_float = float(total_bill)
amount_of_people_int = int(amount_of_people)
tip_amount_int = int(tip_amount)

tip_amount_float = float((total_bill_float * tip_amount_int) / 100)
total_amount_bill_float = float(total_bill_float + tip_amount_float)

if (amount_of_people_int == 0 or amount_of_people_int == 1):
    print(f"Total bill is {round(total_amount_bill_float)}")
elif (amount_of_people_int >= 1):
    print(f"The total bill per person is {round(total_amount_bill_float / amount_of_people_int)}")


