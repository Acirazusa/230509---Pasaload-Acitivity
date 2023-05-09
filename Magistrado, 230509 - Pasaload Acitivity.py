#Magistrado, 230509 - Pasaload Acitivity

import threading

lock = threading.Lock()

def buy_load(mobile_number, amount):
    lock.acquire()
    try:
        # Code to buy load here
        print(f"{amount} pesos load has been successfully bought for mobile number {mobile_number}.")
    finally:
        lock.release()

mobile_number = input("Enter mobile number: ")

while True:
    # Display menu of options
    print("Select an option:")
    print("1. Change mobile number")
    print("2. Buy load")
    print("3. Exit")

    # Prompt user to select an option
    option = input("Enter option number: ")

    if option == "1":
        mobile_number = input("Enter new mobile number: ")
    elif option == "2":
        # Display menu of load amounts
        print("Select amount to buy load:")
        print("1. 10 pesos")
        print("2. 20 pesos")
        print("3. 50 pesos")
        print("4. 100 pesos")

        # Prompt user to select an option
        amount_option = input("Enter option number: ")

        if amount_option == "1":
            amount = 10
        elif amount_option == "2":
            amount = 20
        elif amount_option == "3":
            amount = 50
        elif amount_option == "4":
            amount = 100
        else:
            print("Invalid option selected.")
            continue

        t = threading.Thread(target=buy_load, args=(mobile_number, amount))
        t.start()
        t.join()
    elif option == "3":
        break
    else:
        print("Invalid option selected.")
        continue
