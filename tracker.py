#Laboratory No.5 : Installment 5: The Tracker Menu Comes, Author: Mark John A. Rabago
print("=" * 40)
print("            EXPENSE TRACKER")
print("       Know where your money goes.")
print("=" * 40)

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

subtotal = 0
count = 0

while True:
    print("")
    print("MAIN MENU")
    print("  [1] Add an expense")
    print("  [2] View all expenses (coming soon)")
    print("  [3] Show total spent")
    print("  [4] Exit")
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal = subtotal + amount
        count = count + 1
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        grand_total = subtotal + tax
        print(f"  {'Expenses:':<14}{count}")
        print(f"  {'Subtotal:':<14}${subtotal}")
        print(f"  {'Tax (' + str(tax_percent) + '%):':<14}${tax}")
        print(f"  {'Grand total:':<14}${grand_total}")
        if grand_total > budget:
            print(f"  Over budget by ${grand_total - budget}!")
        elif grand_total > budget * 0.90:
            print(f"  Careful: only ${budget - grand_total} left.")
        else:
            print(f"  Within budget. ${budget - grand_total} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        break

    else:
        print("  Please choose 1, 2, 3 or 4.")

print("-" * 40)
print("Made by: Mark John A. Rabago  |  Installment 5")
print("=" * 40)