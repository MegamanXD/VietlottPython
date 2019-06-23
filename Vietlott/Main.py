from Vietlott import OptionChoser, CustomerList, ShopList

option = -1
customers = CustomerList.CustomerList()
shops = ShopList.ShopList()

while option != 12:
    print("\nPlease choose an option")
    print("1. Add customer          5. Add shop             9. Draw jackpot")
    print("2. Delete customer       6. Delete shop          10. Buy till obtained jackpot")
    print("3. Update customer       7. Update shop          11. Average of 5 buys")
    print("4. View all customers    8. View all shops       12. Quit")
    print("------------------------------------------------------------------------------")
    try:
        option = int(input("Your option: "))
        OptionChoser.perform_option(option, customers, shops)
    except ValueError:
        print("Invalid option! Please enter a number.")
        pass
