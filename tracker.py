#Laboratory No.4 : Installment 4: The Tracker Makes Decisions, Author: Mark John A. Rabago
print("=" * 40)
print("            EXPENSE TRACKER")
print("       Know where your money goes.")
print("=" * 40)     
print("")
print("MAIN MENU")
print("  [1] Add an expense            (coming soon)")
print("  [2] View all expenses         (coming soon)")
print("  [3] Show total spent          (coming soon)")
print("  [4] Exit                      (coming soon)")
print("")

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

firstExpense = input("First expense: ")
amount1 = float(input("Amount of first expense: "))
if amount1 > 200:
    print("    Huge expense - are you sure?")
elif 100 < amount1 <= 200:
    print("    Big expense.")
elif 50 < amount1 <= 100:
    print("    Moderate expense.")
elif 0 <= amount1 <= 50:
    print("    Small expense.")
else:
    print("    Invalid input")

secondExpense = input("Second expense: ")
amount2 = float(input("Amount of second expense: "))
if amount2 > 200:
    print("    Huge expense - are you sure?")
elif 100 < amount2 <= 200:
    print("    Big expense.")
elif 50 < amount2 <= 100:
    print("    Moderate expense.")
elif 50 >= amount2:
    print("    Small expense.")
else:
    print("    Invalid input")

Taxrate = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
if amount1 > 100 and amount2 > 100:
    print("Two big expenses in a row - slow down!")

print("-" * 40)
print("SUMMARY")
print(f"  - {firstExpense}:\t${amount1:.2f}")
print(f"  - {secondExpense}:\t${amount2:.2f}")
Subtotal = 0 + amount1 + amount2
print(f"Subtotal:\t${Subtotal:.2f}")
print(f"Average:\t${Subtotal / 2:.2f}")
print(f"Tax({Taxrate}%):\t${Subtotal * (Taxrate / 100):.2f}")
grandTotal = Subtotal + (Subtotal * (Taxrate / 100))
print(f"Grand Total:\t${grandTotal:.2f}")
if grandTotal > budget:
    print(f"Over budget by ${budget - grandTotal}!")
elif grandTotal > (budget*0.90):
    print(f"Careful: only ${budget - grandTotal} left.")
else:
    print(f"Within budget. ${budget - grandTotal} left.")
print("-" * 40)
print("Made by: Mark John A. Rabago | Installment 3")