print("RHEA WINGS CORNER")
answer = input("Do you want to buy wings? (y/n): ").lower()
wings_1 = 0
wings_2 = 0
wings_3 = 0
wings_0 = 0
if answer.startswith('y'):
    print("1. Buffalo Wings ₱10")
    print("2. Garlic Parmesan Wings ₱12")
    print("3. Spicy Wings ₱15")
    print("4. Cash Out")
    print("5. Exit")
    while(1):
        wingscode = float(input("Input Wings Code: "))
        if (wingscode == 1):
            quantity_1 = float(input("Input Quantity: "))
            wings_0 = wings_0 + 10 * quantity_1
            wings_1 = 10 * quantity_1
            print(f"Subtotal: ₱{wings_1}")
        elif (wingscode == 2):
            quantity_1 = float(input("Input Quantity: "))
            wings_0 = wings_0 + 12 * quantity_1
            wings_2 = 12 * quantity_1
            print(f"Subtotal: ₱{wings_2}")
        elif (wingscode == 3):
            quantity_1 = float(input("Input Quantity: "))
            wings_0 = wings_0 + 15 * quantity_1
            wings_3 = 15 * quantity_1
            print(f"Subtotal: ₱{wings_3}")
        elif (wingscode == 4):
            total = wings_0
            print(f"Total amount: ₱{total}")
            while (2):
                receive = float(input("Input Money Received: "))
                if receive < total:
                    print("Money received is insufficient")
                else:
                    change = receive - total
                    print(f"Your change is: ₱{change}")
                    print("THANK YOU FOR BUYING!")
                    quit()
        elif (wingscode == 5):
            exit()
        else:
            print("Invalid Keyword")
else:
    print("Thank you for using our program!")
    quit()
