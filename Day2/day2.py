def Borders ():
    print(30 * "=-")

Borders()
print("Tip Calculator")
Borders()

total_bill = input("What was the total bill ?\n")
amount_of_people = input("How many people will split this bill ?\n")
tip_amount = input("How much would you like to tip ? None, 5%, 10% or 15%\n")

if (int(amount_of_people) == 0 or int(amount_of_people) == 1):
    print(f"Total bill is {total_bill}")
elif (int(amount_of_people) >= 1):
    print(f"The total bill per person is {int(total_bill) / int(amount_of_people)}")


